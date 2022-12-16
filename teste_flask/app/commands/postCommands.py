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
    select_estado = input('Insira a sigla do Estado[AC,AL,AP,AM,BA,CE,DF,ES,GO,MA,MT,MS,MG,PA,PB,PR,PE,PI,RJ,RN,RS,RO,RR,SC,SP,SE,TO]').upper()
    anos = int(input('Qual a margem de anos que quer analisado (2007 - 2018)'))
    id_imagem =  int(input("Id da imagem a ser postada: "))
    auth = bool(input("Postagem[True/False]: "))
    texto_select = int(input('Escolha um dos modelos de texto[1/2] :'))
    if texto_select == 1:
        texto_postagem = str().format(select_estado,anos)
    else:
        texto_postagem = str('O Estado {},tem pouco acesso a educação a quantidade faltosa acesso á escolas de ensino básico foi um dos piores nos ultimos {} anos:').format(select_estado,anos)
    post = {
        "idPost" : name,
        "select_estado" : select_estado,
        'anos ' : anos,
        "id_imagem" : id_imagem,
        "autorizado" : auth,
        "texto_postagem" : texto_postagem,
        "already_posted" : False
    }

    postExists = postCollection.find_one({"idPost" : name})
    if postExists:
        print(f'O post {name} já foi enviado para o BD')
    else:
        postCollection.insert_one(post)
        print('Post Enviado com sucesso para o BD')
