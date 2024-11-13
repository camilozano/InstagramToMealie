import os
import shutil

from helpers.instadownloader import InstaDownloader
from helpers.mealie_api import MealieAPI

from flask import Flask, request, render_template

if "MEALIE_URL" in os.environ:
    print(os.environ.get("MEALIE_URL"))
else:
    print("You're MEALIE_URL ENV Variable is not set")
    exit(1)

if "MEALIE_API_KEY" in os.environ:
    print("Mealie API Key is set in ENV")
else:
    print("You're MEALIE_API_KEY ENV Variable is not set")
    exit(1)

if "INSTA_USER" in os.environ:
    print("INSTA_USER is set in ENV")
else:
    print("You're INSTA_USER ENV Variable is not set")
    exit(1)

if os.path.isfile("./session-file"):
    print("Session file exists")
else:
    if "INSTA_PWD" in os.environ:
        if "INSTA_TOTP_SECRET" in os.environ:
            print("Insta PWD and TOTP SECRET are set in ENV - trying to login but will possibly fail")
        else:
            print(
                "Insta PWD is set but TOTP SECRET is not set - continue but will fail if 2FA is configured for instagram account")
    else:
        print("Neither session-file nor Insta PWD is configured - recomending session file")
        exit(1)

if "MEALIE_OPENAI_REQUEST_TIMEOUT" in os.environ:
    print(os.environ.get("MEALIE_OPENAI_REQUEST_TIMEOUT"))
else:
    print("You're MEALIE_OPENAI_REQUEST_TIMEOUT ENV Variable is not set - using default of 60")

mealie_api = MealieAPI(os.environ.get("MEALIE_URL"), os.environ.get("MEALIE_API_KEY"))
downloader = InstaDownloader()
print("Startup Successfully")

app = Flask(__name__)


def execute_download(url):
    post = downloader.download_instagram_post(url)
    filepath = "downloads/" + post.shortcode + "/"
    caption_file = filepath + post.date.strftime(format="%Y-%m-%d_%H-%M-%S_UTC") + ".txt"

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

    serve(app, host="0.0.0.0", port=9001)
