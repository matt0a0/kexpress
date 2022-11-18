from pymongo import MongoClient
from flask_pymongo import PyMongo

#Conexão com o MongoDB
client = MongoClient("mongodb+srv://ma90theus:pipocando03@cluster0.zkhtqwe.mongodb.net/Tweets?retryWrites=true&w=majority")

#Conecto com o Cluster Principal (Tweets)
db = client.get_database('Tweets')
#Crio a Base onde eu vou gerar todos os Tweets(10 Tweets Automaticos)
tweetCollection = db.tweetGerado
def geraTweet(id_Imagem):
    name = input("Nome Post :")
    decisao = int(input('Autorizado[1] / Não Autorizado[0] : '))
    texto_postagem = input("Texto a ser Postado : ")
    if decisao == 1:
        state = True
    else:
        state = False
    while len(texto_postagem) > 280:
        print('Insira um texto menor')
        texto_postagem = input("Texto a ser Postado : ")
    post = {
        "idPost" : name,
        "id_imagem" : id_Imagem,
        "autorizado" : state,
        "texto_postagem" : texto_postagem
    }
    auth = state
    tweetCollection.insert_one(post)
for i in range(1,4):
    id_Imagem = i
    geraTweet(id_Imagem)