from flask import Flask
from .route.user import user
from .extensions import database
from .commands.postCommands import postCommands
def create_app():
    app = Flask(__name__)
    app.register_blueprint(user)

    #Conectando e Inicializando o Banco de Dados
    app.config["MONGO_URI"] = "mongodb+srv://ma90theus:pipocando03@cluster0.zkhtqwe.mongodb.net/BaseTeste?retryWrites=true&w=majority"


    #Subindo parte Json
    app.register_blueprint(postCommands)
    database.init_app(app)

    return app
