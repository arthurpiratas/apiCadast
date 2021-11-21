import os
from flask import Flask 
from flask_restx import Api


class Server():

    def __init__(self, ):
        self.app = Flask(__name__)
        self.api = Api(self.app, 
            version='1.0',
            title='Api de Cadastro e Consulta de Clientes',
            description='Api que sera utilizada em uma aplicaco web que consulta clientes', 
            doc='/docs')

    def run(self, ):
        Port = int(os.environ.get("PORT", 5000))
        self.app.run(
            debug=True, #cancelar o debug qnd tiver em produção - alterar debug para False quando subir para o heroku
            host='0.0.0.0', 
            port=Port)

server = Server()