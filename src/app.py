from flask import Flask, request, jsonify
import psycopg2
import os
from decimal import Decimal
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Database connection setup
DB_NAME = os.getenv('POSTGRES_DB', 'Enterprise')
DB_USER = os.getenv('POSTGRES_USER', 'postgres')
DB_PASS = os.getenv('POSTGRES_PASSWORD', 'Student_1234')
DB_PORT = os.getenv('POSTGRES_PORT', '5432')
DB_HOST = 'postgres'

# Check if running within Docker container
DOCKER_CONTAINER = os.getenv('DOCKER_CONTAINER')

if DOCKER_CONTAINER:
    # Running within Docker container, use 'postgres' as hostname
    DB_HOST = 'postgres'
else:
    # Running locally, use 'localhost' as hostname
    DB_HOST = 'localhost'

def get_db_connection():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn

def convert_decimal(data):
    if isinstance(data, list):
        return [convert_decimal(item) for item in data]
    elif isinstance(data, tuple):
        return tuple(convert_decimal(item) for item in data)
    elif isinstance(data, dict):
        return {key: convert_decimal(value) for key, value in data.items()}
    elif isinstance(data, Decimal):
        return float(data)
    else:
        return data

@app.route('/')
def index():
    return "Welcome to the Flask PostgreSQL app!"

# Fetch all employees
@app.route('/employees', methods=['GET'])
def get_employees():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees;')
    employees = cursor.fetchall()
    cursor.close()
    conn.close()
    employees = convert_decimal(employees)  # Convert Decimal types to float
    return jsonify(employees)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
    # Path to SSL/TLS certificate and private key
    # ssl_cert = os.path.join(os.path.dirname(__file__), '.\src\certs\server.crt')
    # ssl_key = os.path.join(os.path.dirname(__file__), '.\src\certs\server.key')
    #
    # # Run Flask app with SSL/TLS
    # app.run(host='0.0.0.0', port=5000, ssl_context=(ssl_cert, ssl_key))
    # app.run(host='0.0.0.0', port=8080, ssl_context=(ssl_cert, ssl_key))