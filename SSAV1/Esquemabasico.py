import psycopg2
from flask import Flask, jsonify
from db import Acceso

app = Flask(__name__)

@app.route('/esquemabasico')
def esquema():
    condiciones = {
        'nombrevacuna': ('IN', ['VPH', 'Rotavirus'])
    }
    data = Acceso("vw_EsquemaBasico").EjecutaVista(condiciones)
    return jsonify(data)

@app.route('/esquemabasico/test')
def esquemafn():
    params = ["10", "5", "20"]
    data = Acceso("funcion_prueba",params).EjecutaFuncion()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)  