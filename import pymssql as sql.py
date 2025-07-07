import pymssql as sql

# Parámetros de conexión
conexion = sql.connect(
    server='PABLOJ-LT',       # o '127.0.0.1'
    user='pablojavierluces@hotmail.com',    # por ejemplo, 'sa'
    password='1508',
    database='PTY',
    port=1433,                # puerto por defecto de SQL Server
    charset='UTF-8',
    as_dict=True              # opcional, para obtener resultados como diccionarios
)

# Ejecutar una consulta de prueba
cursor = conexion.cursor()
cursor.execute("SELECT PTY() AS dbo.PTY_bd;")

for fila in cursor:
    print(f"Conectado a la base de datos: {fila['dbo.PTY_bd']}")

# Cerrar conexión
cursor.close()
conexion.close()
