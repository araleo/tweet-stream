import json
import os

from pymongo import MongoClient
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import StreamListener


class Listener(StreamListener):
    def __init__(self, db):
        super(Listener, self).__init__()
        self.db = db

    def on_data(self, data):
        self.db.tweet.insert_one(json.loads(data))
        return True

    def on_error(self, status_code):
        print(status_code)


def load_cred():
    key = os.environ.get("TWITTER_PUBLIC_KEY", None)
    key_s = os.environ.get("TWITTER_SECRET_KEY", None)
    token = os.environ.get("TWITTER_PUBLIC_TOKEN", None)
    token_s = os.environ.get("TWITTER_SECRET_TOKEN", None)
    return key, key_s, token, token_s


def load_db():
    mongo_user = os.environ.get("MONGO_USER", None)
    mongo_pass = os.environ.get("MONGO_PASS", None)
    if mongo_user is None or mongo_pass is None:
        return None

    conn_string = f"mongodb://{mongo_user}:{mongo_pass}@mongo/twitter?authSource=admin"
    client = MongoClient(conn_string)
    db = client.tweets
    return db


def main():
    key, key_s, token, token_s = load_cred()
    if not all([key, key_s, token, token_s]):
        print("Please enter the Twitter credentials in the .env file.")
        return

    screen_names = os.environ.get("SCREEN_NAMES", None)
    if screen_names is None:
        print("Please enter the desidred screen names to track in the .env file.")
        return

    db = load_db()
    if db is None:
        print("Please enter the MongoDB credentials in the .env file.")
        return

    listener = Listener(db)
    auth = OAuthHandler(key, key_s)
    auth.set_access_token(token, token_s)
    stream = Stream(auth, listener)

    try:
        stream.filter(track=screen_names.split(","))
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
