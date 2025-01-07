import os
import shutil

from helpers.instadownloader import InstaDownloader
from helpers.mealie_api import MealieAPI

from flask import Flask, request, render_template

if "MEALIE_URL" in os.environ:
    print(f"Got Mealie URL: {os.environ.get("MEALIE_URL")} from environment")
else:
    print("Failed to get Mealie URL from environment, make sure MEALIE_URL is set.")
    exit(1)

if "MEALIE_API_KEY" in os.environ:
    print("Got Mealie API key from environment")
else:
    print("Failed to get Mealie API key from environment, make sure MEALIE_API_KEY is set.")
    exit(1)

if "INSTA_USER" in os.environ:
    print(f"Got Instagram username: {os.environ.get("INSTA_USER")} from environment")
else:
    print("Failed to get Instagram username from environment, make sure INSTA_USER is set.")
    exit(1)

if os.path.isfile("./session-file"):
    print("Using the session file at: ./session-file")
else:
    if "INSTA_PWD" in os.environ:
        if "INSTA_TOTP_SECRET" in os.environ:
            print("Got Instagram password and TOTP secret from environment. Trying to login without session file but failure is possible. Authenticating via session file is recommended.")
        else:
            print("Instagram password is set but no TOTP secret was found. Set INSTA_TOTP_SECRET if using 2FA, contuining with regular login without 2FA...")
    else:
        print("Failed to get a session file or Instagram password. Provide a valid session file or set INSTA_PWD in environment")
        exit(1)

if "MEALIE_OPENAI_REQUEST_TIMEOUT" in os.environ:
    print(f"Got OpenAI timeout: {os.environ.get("MEALIE_OPENAI_REQUEST_TIMEOUT")}s from environment")
else:
    print("Failed to get OpenAI timeout from environment. Using the default of 60s, if other timeout is desired make sure MEALIE_OPENAI_REQUEST_TIMEOUT is set.")

mealie_api = MealieAPI(os.environ.get("MEALIE_URL"), os.environ.get("MEALIE_API_KEY"))
downloader = InstaDownloader()
print("Started succesfully")

app = Flask(__name__)


def execute_download(url):
    post = downloader.download_instagram_post(url)
    filepath = "downloads/" + post.shortcode + "/"

    try:
        recipe_slug = mealie_api.create_recipe_from_html(post.caption)

        mealie_api.update_recipe_orig_url(recipe_slug, url)
        image_file = filepath + post.date.strftime(format="%Y-%m-%d_%H-%M-%S_UTC") + ".jpg"
        mealie_api.upload_recipe_image(recipe_slug, image_file)
        if post.is_video:
            video_file = filepath + post.date.strftime(format="%Y-%m-%d_%H-%M-%S_UTC") + ".mp4"
            mealie_api.upload_recipe_asset(recipe_slug, video_file)

        shutil.rmtree(filepath)

        return render_template("index.html", successful="true")

    except Exception as e:
        shutil.rmtree(filepath)
        return repr(e)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        return execute_download(url)

    elif request.args.get('url') is not None and request.args.get('url') != "":
        url = request.args.get('url')
        return execute_download(url)

    return render_template("index.html")


if __name__ == "__main__":
    from waitress import serve

    http_port = os.environ.get("HTTP_PORT") or 9001

    serve(app, host="0.0.0.0", port=http_port)
