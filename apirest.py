from flask import  Flask, jsonify
import pymssql

app = Flask(__name__)

# Configuración de la base de datos
DB_CONFIG = {
    'host': 'PORTATILIAPABLO\PORTATILIA2017',      # Cambia esto por tu servidor SQL Server
    'user': '',     # Usuario de SQL Server
    'password': '',  # Contraseña de SQL Server
    'database': 'pty'   # Nombre de la base de datos
}

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/bancos', methods=['GET'])
def get_users():
    try:
        # Conectar a la base de datos
        conn = pymssql.connect(**DB_CONFIG)
        cursor = conn.cursor()
 
        # Ejecutar consulta
        cursor.execute("SELECT * FROM bancos")  # Asegúrate de que la tabla exista
        print("Consulta ejecutada")
        # Obtener resultados
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        print("Columnas obtenidas:", rows)
        return jsonify(rows)
        # Convertir a JSON
        result = [dict(zip(columns, row)) for row in rows]

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if 'conn' in locals():
            conn.close(
                
            )

@app.route('/api/bancos/<int:banco_id>', methods=['GET'])
def get_banco_by_id(banco_id):
    try:
        # Conectar a la base de datos
        conn = pymssql.connect(**DB_CONFIG)
        cursor = conn.cursor()
 
        # Ejecutar consulta con parámetro ID
        cursor.execute("SELECT * FROM bancos WHERE codbank= %s", (banco_id,))
        print(f"Consulta ejecutada para banco ID: {banco_id}")
        
        # Obtener resultado
        row = cursor.fetchone()
        
        if row is None:
            return jsonify({"error": "Banco no encontrado"}), 404
        
        # Obtener nombres de columnas
        columns = [desc[0] for desc in cursor.description]
        
        # Convertir a JSON
        result = dict(zip(columns, row))
        
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if 'conn' in locals():
            conn.close()

@app.route('/api/bancosi/<codbank>/<nombre>', methods=['GET'])
def create_bank(codbank, nombre):
    print(f"Creando banco con codbank: {codbank}, nombre: {nombre}")
    try:
        conn = pymssql.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Ejecutar inserción
        cursor.execute("""
            INSERT INTO bancos (codbank, descbank)
            VALUES (%s, %s)
        """, (codbank, nombre))

        conn.commit()
        return jsonify({"mensaje": "Banco creado exitosamente", "nombre": nombre, "codbank": codbank}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
