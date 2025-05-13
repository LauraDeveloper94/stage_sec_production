#!/usr/bin/env python3

from flask import Flask, jsonify
from datetime import date
import random

# Me creo una API REST con Flask con dos endpoints para obtener datos simulados sobre la producción de una máquina de montaje, 
# incluyendo la fecha actual y una cantidad aleatoria de productos producidos. Cada endpoint devuelve los datos en formato JSON.

app = Flask(__name__)
 

@app.route('/machineryData/info', methods=['GET'])
def info_maquina():

    data = {
        "machinery": "Assembly",
        "date": str(date.today().isoformat()),
        "production": random.randint(1, 10)
    }

    return jsonify(data)

@app.route('/machineryData/data', methods=['GET'])
def datos_maquina():
    product_qt = random.randint(20, 50)

    data = {
        "machinery": "Assembly",
        "date": str(date.today().isoformat()),
        "production": product_qt
    } 
    
    return jsonify(data) 

    #colección de datos de todo el día

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
