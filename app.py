import os
import socket
from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)
DB_URI = os.environ.get('DB_URI')
hostname = socket.gethostname()

def get_db_connection():
    return psycopg2.connect(DB_URI)

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT rut, nombre, telefono FROM clientes;')
        clientes = cur.fetchall()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error de BD: {e}")
        clientes = []
    return render_template('index.html', clientes=clientes, hostname=hostname)

@app.route('/guardar', methods=['POST'])
def guardar():
    rut = request.form['rut']
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO clientes (rut, nombre, telefono) VALUES (%s, %s, %s)
            ON CONFLICT (rut) DO UPDATE SET nombre = EXCLUDED.nombre, telefono = EXCLUDED.telefono;
        ''', (rut, nombre, telefono))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error al guardar: {e}")
    return redirect('/')

@app.route('/eliminar/<rut>')
def eliminar(rut):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('DELETE FROM clientes WHERE rut = %s;', (rut,))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error al eliminar: {e}")
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)