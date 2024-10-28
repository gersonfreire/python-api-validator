from flask import Flask, jsonify
from controllers.cpf_controller import CPFController
from controllers.cnpj_controller import CNPJController

app = Flask(__name__)

@app.route('/validarCpf/<cpf>', methods=['GET'])
def validar_cpf(cpf):
    response = CPFController.validar_cpf(cpf)
    return jsonify(response)

@app.route('/gerarCpf', methods=['GET'])
def gerar_cpf():
    response = CPFController.gerar_cpf()
    return jsonify(response)

@app.route('/validarCnpj/<cnpj>', methods=['GET'])
def validar_cnpj(cnpj):
    response = CNPJController.validar_cnpj(cnpj)
    return jsonify(response)

@app.route('/gerarCnpj', methods=['GET'])
def gerar_cnpj():
    response = CNPJController.gerar_cnpj()
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=9002, debug=True)