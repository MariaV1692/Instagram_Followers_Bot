from InstaBot import InstaFollower
import os
from dotenv import load_dotenv

load_dotenv()

email = os.environ["EMAIL"]
password = os.environ["PASSWORD"]
account_to_find = os.environ["SIMILAR_ACCOUNT_NAME"]

insta_bot = InstaFollower()
insta_bot.login_to_instagram(email=email, password=password)
insta_bot.find_followers(account_to_find=account_to_find)
insta_bot.follow()
