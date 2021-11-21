from json import dump, load
from flask import Flask, request, json, jsonify, render_template
from os.path import dirname, isfile, realpath
import requests
import json
from werkzeug.utils import redirect

app = Flask(__name__, template_folder='templates', static_folder='static')

# CRIA JSON SE N EXISTIR


class JsonMananger:
    def __init__(self):
        self.path = dirname(realpath(__file__)) + '/'

    def create_json(self, file):
        data = {"inicio": "", "json": ""}
        path_data_json = self.path + file

        if not isfile(path_data_json):
            with open(path_data_json, 'w') as f:
                dump(data, f, indent=2, separators=(',', ': '))
            return True
        else:
            return False

    # CRIA JSON SE N EXISTIR

    # GRAVA NO JSON
    def grava_json(self, file):
        nome = request.form.get('nome')
        contato = request.form.get('contato')
        email = request.form.get('email')
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        placa = request.form.get('placa')

        # DICIONARIO DO ITEM ATUAL
        dici = {
            'nome': nome,
            'contato': contato,
            'email': email,
            'latitude': latitude,
            'longitude': longitude,
            'placa': placa,

        }
        arq = open(file, mode='r')
        dados = json.load(arq)
        dados = [d for d in dados]
        dados.append(dici)
        arq.close()
        arq = open(file, mode='w')
        arq.write(json.dumps(dados, indent=2))

    # GRAVA NO JSON

    # LER NO JSON
    def ler_json(self, file):
        if isfile(self.path + file):
            with open(self.path + file) as f:
                data = load(f)
            return data
        else:
            return False
    # LER NO JSON


@app.route("/", methods=['get'])
def index():
    return render_template('index.html')


@app.route("/cadastro")
def cadastro():
    return render_template('cadastro.html')


@app.route("/pesquisa")
def pesquisa():
    return render_template('pesquisa.html')


@app.route("/salvar", methods=['post'])
def salvar():
    jmanager = JsonMananger()
    jmanager.create_json('BD.json')
    jmanager.grava_json('BD.json')
    return redirect('/')


@app.route("/data")
def data():
    jmanager = JsonMananger()
    JSON_BD = jmanager.ler_json('BD.json')  # json onde fica os 'BD'
    return jsonify(JSON_BD)

if __name__ == '__main__':
    app.run()
