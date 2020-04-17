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
@app.route('/Conteo_Registros')
def count():
    rs= cursor.execute("select sum(to_number(extractvalue(xmltype(dbms_xmlgen.getxml(\'select count(*) c from \'||table_name)),\'/ROWSET/ROW/C\'))) count from user_tables")
    return print(rs.fetchall())


#Insertar EMPLEADO, PUESTO, REGION, PAIS, LOCATION 
@app.route('/Insertar')
def insertar():
    return 'Insertar'

#Actualizar puesto, salario de EMPLEADO (por id)
@app.route('/Actualizar')
def actualizar():
    return 'Actualizar'

#Eliminar EMPLEADO (por id)
@app.route('/Eliminar')
def eliminar():
    return 'Eliminar'

#Consultar Empleado (por id)
@app.route('/Consultar')
def consultar():
    return 'Consultar'


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)