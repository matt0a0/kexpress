from flask import Flask
from extensions import database
from .commands.get_info import getInfo

def create_app():
    app = Flask(__name__)
    #Conectando Banco de Dados
    app.config["MONGO_URI"] = "mongodb+srv://ma90theus:pipocando03@cluster0.zkhtqwe.mongodb.net/BaseTeste?retryWrites=true&w=majority"

    #Subindo parte Json
    app.register_blueprint(getInfo)
    database.init_app(app)

    return app

