from json import dump, load
from flask import Flask, request, json, render_template
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
            return True;
        else:
            return False;

    # CRIA JSON SE N EXISTIR

    # GRAVA NO JSON
    def grava_json(self, file):
        eletrodomestico = request.form.get('eletrodomestico')
        req = requests.get('https://happliance.herokuapp.com/api/v1/appliances/name?name=' + eletrodomestico).json()
        potencia = req['power']
        nome = request.form.get('nome')
        horas = request.form.get('horas')
        dias = request.form.get('dias')

          # DICIONARIO DO ITEM ATUAL
        dici = {
            'nome': nome,
            'eletrodomestico': eletrodomestico,
            'potencia': potencia,
            'horas': horas,
            'dias': dias,
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
            with  open(self.path + file) as f:
                data = load(f)
            return data
        else:
            return False
    # LER NO JSON


@app.route("/", methods=['get'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
