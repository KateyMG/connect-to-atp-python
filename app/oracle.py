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
    data = request.get_json()
    opt = data.get('opt')
    

    if opt == 'insert_employee':
        e_id = data.get('id')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        phone_number = data.get('phone_number')
        hire_date = data.get('hire_date')
        job_id = data.get('job_id')
        salary = data.get('salary')
        comission_pct = data.get('comission_pct')
        manager_id = data.get('manager_id')
        department_id = data.get('department_id')
        sql = """insert into employees 
            (
                employee_id, 
                first_name, 
                last_name, 
                email, 
                phone_number, 
                hire_date, 
                job_id, 
                salary, 
                comission_pct, 
                manager_id, 
                department_id
            )
        values 
            (
                :employee_id, 
                :first_name, 
                :last_name, 
                :email, 
                :phone_number, 
                to_date(:hire_date, 'YYYY-MM-DD'), 
                :job_id, 
                :salary, 
                :comission_pct, 
                :manager_id, 
                :department_id
            );"""

        values = [  
            e_id, 
            first_name, 
            last_name, 
            email, 
            phone_number, 
            hire_date, 
            job_id, 
            salary, 
            comission_pct, 
            manager_id, 
            department_id
            ]
        rs = cursor.execute(sql, values)
        connection.commit()
    return 'Se ha insertado un empleado'

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
        where employee_id = :id"""
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
    data = request.get_json()
    action = data.get('action')

    if action == "eliminar":
        id = data.get('id')
        sql = """delete from employees
        where employee_id = :id"""
        values = [
            id]
        rs = cursor.execute(sql, values)
        connection.commit()
    return 'Se ha eliminado'

#Consultar Empleado (por id)
@app.route('/Consultar')
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