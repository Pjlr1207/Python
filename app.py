"""
✅ OPCIONES DE PROYECTO PARA ELEGIR

Elige UNA de las siguientes API para desarrollar con Flask:

------------------------------------------------------------
⿡ API DE FRUTAS FAVORITAS 🍎

- Permite registrar y consultar una lista de frutas favoritas.
- Datos en memoria (lista o Diccionario).
- Cada fruta tiene un id autogenerado."""

from flask import Flask, jsonify 
app=Flask(__name__)
#Listado para almacenar frutas y sus id 
lista_frutas =[]
id_lista = 1 #Variable unica para id de frutas

# mensade conexion al API
@app.route('/', methods=['GET'])  
def fruit():
    return jsonify({'mensaje': 'Bienvenido al Api de frutas'})

@app.route('/lista', methods=['GET'])
def lista():
    return jsonify({'frutas': lista_frutas})

@app.route ('/agregar/<nombre>', methods=['GET'])
def agregar_fruta(nombre):
    global id_lista
    fruta={
        'id' : id_lista,
        'nombre': nombre
    }
    lista_frutas.append(fruta)
    
    mensaje= f'{nombre} agregada correctamente con el id {id_lista}'
    id_lista += 1
    return jsonify({'mensaje' : mensaje, })

if __name__ == '__main__':
    app.run (debug=False)
