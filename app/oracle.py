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

#Conteo de registros de todas las tablas de HR
@app.route('/Conteo_Registros')
def count():
    rs= cursor.execute("select sum(to_number(extractvalue(xmltype(dbms_xmlgen.getxml(\'select count(*) c from \'||table_name)),\'/ROWSET/ROW/C\'))) count from user_tables")
    return str(rs.fetchall())


#Insertar EMPLEADO, PUESTO, REGION, PAIS, LOCATION 
@app.route('/Insertar')
def insertar():
    return 'Insertar'

#Actualizar puesto, salario de EMPLEADO (por id)
@app.route('/Actualizar')
def actualizar():
    data = request.get_json()
    action = data.get('action')

    if action == "actualizar":
        id = data.get('id')
        salary = data.get('salary')
        job_id = data.get('job_id')
        sql = """update employees 
        set salary = :salary, job_id = :job_id 
        where employee_id = :employee_id"""
        values = [
            salary,
            job_id,
            id
        ]
        rs = cursor.execute(sql, values)
        connection.commit()
    return 'Se ha Actualizado'

#Eliminar EMPLEADO (por id)
@app.route('/Eliminar')
def eliminar():
    return 'Eliminar'

#Consultar Empleado (por id)
@app.route('/Consultar', methods=['GET'])
def consultar():
    data = request.get_json()
    action = data.get('action')
    
    if action == "consultar":
        id = data.get('id')
        sql = """select * 
        from employees 
        where employee_id = :id
        """
        values = [id]
        rs = cursor.execute(sql, values)
        connection.commit()
        return str(rs.fetchall())
    
    


@app.route('/')
def hello_world():
    return 'Hello, World! Hola Mundo'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)