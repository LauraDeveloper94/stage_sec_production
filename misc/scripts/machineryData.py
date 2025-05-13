""" #!/usr/bin/env python3

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
 """

from flask import Flask, jsonify
from datetime import date
import random

# Me creo una API REST con Flask para obtener datos simulados sobre la producción de cada una de las máquinas

app = Flask(__name__)

MACHINES = {
    "assembly": "Assembly",
    "cutting": "Cutting Saw",
    "painting": "Painter",
    "welding": "MIG Welder"
}

@app.route('/machineryData/info/<machine>', methods=['GET'])
def info_maquina(machine):
    if machine not in MACHINES:
        return jsonify({"error": "Machine not found"}), 404

    data = {
        "machinery": MACHINES[machine],
        "date": str(date.today().isoformat()),
        "production": random.randint(1, 10)
    }
    return jsonify(data)

@app.route('/machineryData/data/<machine>', methods=['GET'])
def datos_maquina(machine):
    if machine not in MACHINES:
        return jsonify({"error": "Machine not found"}), 404

    data = {
        "machinery": MACHINES[machine],
        "date": str(date.today().isoformat()),
        "production": random.randint(20, 50)
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

""" URLs:
http://localhost:5000/machineryData/info/assembly
http://localhost:5000/machineryData/info/cutting
http://localhost:5000/machineryData/info/painting
http://localhost:5000/machineryData/info/welding

http://localhost:5000/machineryData/data/assembly
http://localhost:5000/machineryData/data/cutting
http://localhost:5000/machineryData/data/painting
http://localhost:5000/machineryData/data/welding

 """
 