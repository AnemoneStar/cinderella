import os
import twitter
import requests
required_envs = [
    "TWITTER_CONSUMER_KEY",
    "TWITTER_CONSUMER_SECRET",
    "TWITTER_ACCESS_TOKEN",
    "TWITTER_ACCESS_SECRET",
]
notfound_envs = list(filter(lambda x:os.environ.get(x) == None, required_envs))
if len(notfound_envs):
    print("以下の環境変数が必要ですが、設定されていませんでした\n- "+"\n- ".join(notfound_envs))
    exit(1)

TWITTER_API = os.environ.get("TWITTER_API", "https://api.twitter.com/1.1/")

tw = twitter.Twitter(auth=twitter.OAuth(
    os.environ["TWITTER_ACCESS_TOKEN"],
    os.environ["TWITTER_ACCESS_SECRET"],
    os.environ["TWITTER_CONSUMER_KEY"],
    os.environ["TWITTER_CONSUMER_SECRET"],
))

max_id=None

while True:
    a = {
        "count": 200,
        "tweet_mode": "extended"
    }
    if max_id is not None:
        a["max_id"] = max_id
    print(a)
    r = tw.statuses.user_timeline(**a)
    print(r)
    if len(r) == 0:
        break
    for tweet in r:
        max_id = tweet["id_str"]
        if tweet.get("retweeted_status") is None:
            if tweet["favorited"]:
                continue
            if tweet["retweet_count"] != 0:
                continue
            if len(tweet.get("entities", {}).get("user_mentions", [])):
                continue
        print(tweet["full_text"])
        if os.environ.get("TWEET_LOG_POST_URL") is not None:
            print(requests.post(os.environ["TWEET_LOG_POST_URL"], json=tweet))
        tw.statuses.destroy(_id=tweet["id_str"])