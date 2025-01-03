import psycopg2
from flask import Flask, jsonify
from db import Acceso

app = Flask(__name__)

@app.route('/Paciente/Sesion/<curp>')
def SesionPaciente(curp):
    condiciones = {
        'curp': ('=', curp)
    }
    vwSesionPaciente_ = Acceso("vwSesionPaciente").EjecutaVista(condiciones)

    return jsonify(vwSesionPaciente_)


if __name__ == '__main__':
    app.run(debug=True)  
