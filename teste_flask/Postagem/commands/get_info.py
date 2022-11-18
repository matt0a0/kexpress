import click
from ..extensions.database import mongo
from flask import Blueprint

getInfo= Blueprint('getInfo',__name__)

#Buscando Post
@getInfo.cli.command('getPost')
@click.argument('name')
def buscar_Post(name):
    postCollection = mongo.db.posts #Armazeno a coleção de Posts do DB
    post = [p for p in postCollection.find({name : "idPost"})] #Percorre a lista local
    print(post) #Se tiver o id que quero,vai ser escrito na tela
