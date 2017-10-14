import os
from requests_oauthlib import OAuth1Session
required_envs = [
    "TWITTER_CONSUMER_KEY",
    "TWITTER_CONSUMER_SECRET",
    "TWITTER_ACCESS_TOKEN",
    "TWITTER_ACCESS_SECRET",
]
notfound_envs = list(filter(lambda x:os.environ.get(x) == None, required_envs))
if len(notfound_envs):
    print("以下の環境変数が必要ですが、設定されていませんでした\n- "+"\n- ".join(notfound_envs))

twreq = OAuth1Session(
    os.environ["TWITTER_CONSUMER_KEY"]
    os.environ["TWITTER_CONSUMER_SECRET"]
    os.environ["TWITTER_ACCESS_TOKEN"]
    os.environ["TWITTER_ACCESS_SECRET"]
)
TWITTER_API = os.environ.get("TWITTER_API", "https://api.twitter.com/1.1/")

twreq.get("https://twitter.com")
