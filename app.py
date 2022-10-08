import json

from flask import Flask, jsonify, request

app = Flask(__name__)

desenvolvedores = [
    {'nome': 'Heraldo',
     'habilidades': ['Python', 'HTML']},
    {'nome': 'Giovane',
     'habilidades': ['Java', 'Django']}
]

## Devolve um desenvolvedor pelo ID, também altera e remove um desenvolvedor
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'erro', 'mensagem': f'Desenvolvedor de ID {id} não existe.'}
        except Exception:
            response = {'status': 'erro', 'mensagem': 'Erro desconhecido. Procure o adminstrador da API.'}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'Sucesso!!!!', 'mensagem': 'Registro excluído!'})


## Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
@app.route('/dev/', methods = ['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({'status': 'Sucesso', 'mensagem': 'Registro inserido'})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)
