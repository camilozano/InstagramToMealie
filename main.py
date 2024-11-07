import os
import shutil

from helpers.instadownloader import InstaDownloader
from helpers.mealie_api import MealieAPI

from flask import Flask, request, render_template

print(os.environ.get("MEALIE_URL"))
mealie_api = MealieAPI(os.environ.get("MEALIE_URL"), os.environ.get("MEALIE_API_KEY"))
downloader = InstaDownloader()
print("Startup Successfully")

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
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

            return render_template("index.html", successful="true")

        except Exception as e:
            return repr(e)

        shutil.rmtree(filepath)

    return render_template("index.html")


if __name__ == "__main__":
    from waitress import serve

    serve(app, host="0.0.0.0", port=9001)
