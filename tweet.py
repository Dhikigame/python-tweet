#coding: UTF-8
import twitter
import json
import key

#twitter = OAuth1Session(settings.CONSUMER_KEY, settings.CONSUMER_SECRET, settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
api = twitter.Api(consumer_key=key.CONSUMER_KEY,
                  consumer_secret=key.CONSUMER_SECRET,
                  access_token_key=key.ACCESS_TOKEN,
                  access_token_secret=key.ACCESS_TOKEN_SECRET
                  )

api.PostUpdate("Hello Wolrd!")