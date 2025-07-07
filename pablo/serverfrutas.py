from flask import Flask, jsonify  # Importa las clases Flask y jsonify del módulo flask
import json  # Importa el módulo json para trabajar con datos JSON

app = Flask(__name__)  # Crea una instancia de la aplicación Flask

# Cargar datos desde JSON
with open('frutas.json', 'r') as f:  # Abre el archivo 'frutas.json' en modo lectura
    frutas_data = json.load(f)  # Carga los datos JSON del archivo en la variable frutas_data

@app.route('/frutas', methods=['GET'])  # Define una ruta para la URL '/frutas' que solo acepta solicitudes GET
def obtener_frutas():  # Define la función que se ejecutará cuando se acceda a la ruta
    return jsonify(frutas_data)  # Retorna los datos de frutas_data en formato JSON

@app.route('/frutas/color/<color>', methods=['GET'])  # Define una ruta para la URL '/frutas/color/<color>' (donde <color> es una variable) que solo acepta solicitudes GET
def obtener_frutas_por_color(color):  # Define la función que se ejecutará cuando se acceda a la ruta
    frutas_filtradas = [f for f in frutas_data if color.lower() in f['colores']]  # Filtra las frutas por color (insensible a mayúsculas/minúsculas)
    return jsonify(frutas_filtradas)  # Retorna las frutas filtradas en formato JSON

if __name__ == '__main__':  # Verifica si el script se está ejecutando como programa principal
    app.run(debug=True)  # Inicia el servidor de desarrollo de Flask en modo depuración

