import psycopg2
from flask import Flask, jsonify
from db import Acceso

app = Flask(__name__)

@app.route('/Paciente/Home/<curp>')
def EsquemaBasicoPaciente(curp):
    condiciones = {
        'curp': ('=', curp)
    }
    vwEsquemaBasicoPaciente_ = Acceso("vwEsquemaBasicoPaciente").EjecutaVista(condiciones)
    vwSiguientesVacPaciente_ = Acceso("vwSiguientesVacPaciente").EjecutaVista(condiciones)
    vwOtrasVacPaciente_ = Acceso("vwOtrasVacPaciente").EjecutaVista(condiciones)
    Respuesta = {
        'vwEsquemaBasicoPaciente':vwEsquemaBasicoPaciente_,
        'vwSiguientesVacPaciente':vwSiguientesVacPaciente_,
        'vwOtrasVacPaciente':vwOtrasVacPaciente_
    }
    return jsonify(Respuesta)






#@app.route('/esquemabasico/test')
#def esquemafn():
#    params = ["10", "5", "20"]
#    data = Acceso("funcion_prueba",params).EjecutaFuncion()
#    return jsonify(data)
#
if __name__ == '__main__':
    app.run(debug=True)  