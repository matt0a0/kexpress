from turtle import Screen
import tweepy

consumer_key = "iMjbCfuHuqFbMevNdL9SljJ8c"
consumer_secret ="PklMYc6j443Tpttk3ZP01jLo1UK8L8wHeb3CI9HM50vo1ArMUD"
access_token ="1578404739582201857-bnCMYDmPJeOD1GOQBT49Cij6gPkR3j"
access_token_secret ="CZjbz0YfLM1c1KcQpSdRk45x9ciMmMu3ra4Hj3PY1Lj91"

client = tweepy.Client(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

tweet = client.create_tweet(text="Oi pessoal")