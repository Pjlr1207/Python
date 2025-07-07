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

#inicializando lista de frutas
@app.route('/lista', methods=['GET']) #ruta para consultar la lista
def lista(): #funcion lista
    if not lista_frutas:
        return jsonify({'mensaje': 'lista vacia, por favor agregue un producto'}) #verifica si esta vacia la lista
    return jsonify({'frutas': lista_frutas})

@app.route ('/agregar/<nombre>', methods=['GET'])#ruta para agregar frutas
def agregar_fruta(nombre): #define lafuncion para agregar frutas
    global id_lista #define la variable global id_lista
    fruta={
        'id' : id_lista,
        'nombre': nombre
    }
    lista_frutas.append(fruta) #agrega fruta a la lista
    
    mensaje= f'{nombre} agregada correctamente con el id {id_lista}'
    id_lista += 1
    return jsonify({'mensaje' : mensaje, })

if __name__ == '__main__': # ejecuta el archivo
    app.run (debug=False)
