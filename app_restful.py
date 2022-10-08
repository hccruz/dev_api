from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'nome': 'Heraldo',
     'habilidades': ['Python', 'HTML']},
    {'nome': 'Giovane',
     'habilidades': ['Java', 'Django']}
]


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'erro', 'mensagem': f'Desenvolvedor de ID {id} não existe.'}
        except Exception:
            response = {'status': 'erro', 'mensagem': 'Erro desconhecido. Procure o adminstrador da API.'}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'Sucesso!!!!', 'mensagem': 'Registro excluído!'}


class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return {'status': 'Sucesso', 'mensagem': 'Registro inserido'}


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)
