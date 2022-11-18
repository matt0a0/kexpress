from flask_pymongo import PyMongo

mongo = PyMongo() #Intancia da classe PyMongo

#Inicia o mongo quando o App é iniciado também
def init_app(app):
    return mongo.init_app(app)