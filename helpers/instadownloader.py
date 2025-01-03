import os
import re
import instaloader
import pyotp
from instaloader import Post, TwoFactorAuthRequiredException, BadCredentialsException


class InstaDownloader:
    def __init__(self):
        self.loader = instaloader.Instaloader(download_comments=False,
                                              download_geotags=False,
                                              save_metadata=False,
                                              dirname_pattern="downloads/{target}", )
        try:
            user = os.environ.get('INSTA_USER')
            if os.path.isfile("./session-file"):
                self.loader.load_session_from_file(user, "./session-file")
            else:
                self.loader.login(os.environ.get("INSTA_USER"), os.environ.get("INSTA_PWD"))
        except TwoFactorAuthRequiredException:  # Probably not going to work https://github.com/instaloader/instaloader/issues/1217
            print(os.environ.get("INSTA_TOTP_SECRET"))
            totp = pyotp.TOTP(os.environ.get("INSTA_TOTP_SECRET"))
            print(totp.now())
            try:
                self.loader.two_factor_login(totp.now())
            except BadCredentialsException:
                self.loader.two_factor_login(totp.now())

        print(self.loader.test_login())

    def download_instagram_post(self, url) -> Post | None:
        # Validate and extract shortcode from the URL
        match = re.search(r'(https?://)?(www\.)?instagram\.com/(p|reel|tv)/([A-Za-z0-9_-]+)', url)
        if not match:
            print(f"Received invalid Instagram URL ({url}). Please make sure it is a post, reel, or IGTV URL.")
            return None

        shortcode = match.group(4)  # Extract the shortcode from the URL

        try:
            # Load and download the post using the shortcode
            post = instaloader.Post.from_shortcode(self.loader.context, shortcode)
            self.loader.download_post(post, target=post.shortcode)
            print(f"Downloaded post: {url}")
            return post
        except Exception as e:
            print(f"Error downloading post: {e}")
