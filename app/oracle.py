import cx_Oracle
import os
import flask
from flask import Flask, jsonify, request
app = Flask(__name__)
connection = cx_Oracle.connect(os.environ['DB_USER'], os.environ['DB_PASSWORD'], os.environ['DB_CONNECTIONSTRING'])

cursor = connection.cursor()
rs = cursor.execute("select 'Hello for ADB' from dual")
print(rs.fetchall())
rs = cursor.execute("select current_timestamp from dual")
print(rs.fetchall())
rs = cursor.execute("select * from employees")
print(rs.fetchall())
print('hola')

#Conteo de registros de todas las tablas de HR

#Insertar EMPLEADO, PUESTO, REGION, PAIS, LOCATION 

#Actualizar puesto, salario de EMPLEADO (por id)

#Eliminar EMPLEADO (por id)

#Consultar Empleado (por id)


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)