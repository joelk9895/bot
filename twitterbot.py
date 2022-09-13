import tweepy
import key
import openai
from win10toast import ToastNotifier
import time

toast = ToastNotifier()

toast.show_toast("Twitterbot", "Twitterbot has been started.")



openai.organization = "org-DknYGMUv4hVVfzm8aDjzPaOn"
openai.api_key = key.openai_key

def tweetbody():
    response = openai.Completion.create(
    model="text-davinci-001",
     prompt= "tweet something cool for #techtwitter",
    max_tokens = 32
    )
    tweet1 = response["choices"][0]["text"]
    return tweet1
def api():
    auth = tweepy.OAuthHandler(key.api_key, key.api_secret,)
    auth.set_access_token(key.access_token, key.access_secret)

    return tweepy.API(auth)

def tweet(api: tweepy.API, message:str, image_path = None):
    if image_path:
        api.update_status_with_media(message, image_path)
    else:
        api.update_status(message)

if __name__ == "__main__":
    api = api()
    n = 0
    while n == 0:
        message1 = tweetbody()
        tweet(api, message1)
        toast.show_toast("Twitterbot tweeted", message1)
        time.sleep(36000)