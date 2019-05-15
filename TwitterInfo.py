import tweepy

consumer_key = '2sPoXxKFmM1tsYqIlePFZ6wxD'
consumer_secret = 'dD20E2nHN2BfP6lQN4a9O1jechJF6iEenoPLWqII0ZVFTnqZlt'
access_token = '239766287-xr4zRE721NLhJRmojhlf3vzbQZlIoM6xL1ENCuc4'
access_token_secret = '9VRjw7cYn0S6Q2X8J24vVuIzFnayDey00F6hJAKHQx3K5'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


user = api.me()
print(user.name)

