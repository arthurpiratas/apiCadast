from flask import Flask, jsonify, request
from flask_restx import Api, Resource
from flask_cors import CORS

from src.server.instance import server

app, api = server.app, server.api

CORS(app)

@api.route('/ListaCadastro', methods=['GET'])
class listaEventos(Resource):
    def get(Self, ):
        return "Arthur", 200
