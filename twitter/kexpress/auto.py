from turtle import Screen
import tweepy
from pymongo import MongoClient
import time

CONSUMER_KEY = "8yFjTO9EjWUU8iNgWuajCa8qh"
CONSUMER_SECRET ="JghQZHFxYHGyrxxIk0FPSCikrWgzS8O4NAd7NjmNpTSSpgOxeZ"
ACCESS_TOKEN ="1583178044365279239-jd1Sj7iPpWVkYlr3RUCGJHoSfixjDP"
ACCESS_TOKEN_SECRET ="WThUszj4dtR5kqp3wtxnEehue17jAPbelZAdvwqdIfXPY"

client = tweepy.Client(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

#Conexão entre o mongodb e o app
clientMongo = MongoClient("mongodb+srv://ma90theus:<senha de administrador>@cluster0.zkhtqwe.mongodb.net/?retryWrites=true&w=majority")
#Acessando meu db específico
db = clientMongo['Tweets']
#Acessando todos os documentos presentes no meu Collum
coll = db['tweetGerado']

#Selecionando todos o que estão com a publicação validada
for i in coll.find({"autorizado" : True},{}):
    publi = i['texto_postagem']
    #Aplico o Looped Time
    #Set do temporizador da publicação
    begin_clock = time.time()
    clock_timer = 60
    while True:
        current_clock = time.time()
        past_clock = current_clock - begin_clock
        if past_clock > clock_timer:
            print("O sistema de postagem foi iniciado\n ----------Tempo para a próxima postagem{}".format(clock_timer))
            #Realizo a postagem
            tweet = client.create_tweet(text=publi)
            print("###O tweet :  {} foi publicado!".format(tweet))
            break 
