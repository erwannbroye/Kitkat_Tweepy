from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

#add your keys

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

class StdOutListener(StreamListener):
    def on_data(self, data):
        data = json.loads(data)
        # print(json.dumps(data, indent=4, sort_keys=True))
        print(data["created_at"])
        print(data["user"]["name"])
        print(data["text"])
        print("\n")

    def on_error(self, status):
        print(status)

listener = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, listener)

stream.filter(track=['Python', 'Donald Trump'])
