import click
from ..extensions.database import mongo
from flask import Blueprint

postCommands = Blueprint('post',__name__)

#Buscando Post
@postCommands.cli.command('getPost')
@click.argument('name')
def buscar_Post(name):
    postCollection = mongo.db.posts #Armazeno a coleção de Posts do DB
    post = [p for p in postCollection.find({name : "idPost"})] #Percorre a lista local
    print(post) #Se tiver o id que quero,vai ser escrito na tela

#Adicionando Post
@postCommands.cli.command("addPost")
@click.argument('name')
def add_Post(name):
    postCollection = mongo.db.posts
    id_imagem =  int(input("Id da imagem a ser postada: "))
    auth = bool(input("Postagem[True/False]: "))
    texto_postagem = input("Texto a ser Postado : ")
    post = {
        "idPost" : name,
        "id_imagem" : id_imagem,
        "autorizado" : auth,
        "texto_postagem" : texto_postagem
    }

    postExists = postCollection.find_one({"idPost" : name})
    if postExists:
        print(f'O post {name} já foi enviado para o BD')
    else:
        postCollection.insert_one(post)
        print('Post Enviado com sucesso para o BD')
