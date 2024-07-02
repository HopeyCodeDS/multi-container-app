import psycopg2
import os
from flask import Flask, jsonify
from decimal import Decimal
from dotenv import load_dotenv
import time

load_dotenv()

app = Flask(__name__)

# Database connection setup
DB_NAME = os.getenv('POSTGRES_DB', 'Enterprise')
DB_USER = os.getenv('POSTGRES_USER', 'postgres')
DB_PASS = os.getenv('POSTGRES_PASSWORD', 'Student_1234')
DB_PORT = os.getenv('POSTGRES_PORT', '5432')
DB_HOST = 'postgres'  # Ensure this matches the service name in docker-compose.yml

def get_db_connection(retries=5):
    attempts = 0
    while attempts < retries:
        try:
            conn = psycopg2.connect(
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASS,
                host=DB_HOST,
                port=DB_PORT
            )
            return conn
        except psycopg2.OperationalError as e:
            print(f"Connection attempt {attempts + 1} failed: {e}")
            attempts += 1
            time.sleep(2)  # Wait for 2 seconds before retrying

    raise Exception(f"Failed to connect to database after {retries} attempts.")

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create employees table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS employees (
        employee_id   CHAR(9)      NOT NULL,
        last_name     VARCHAR(25)  NOT NULL,
        first_name    VARCHAR(25)  NOT NULL,
        infix         VARCHAR(25),
        street        VARCHAR(50),
        location      VARCHAR(25),
        province      CHAR(2),
        postal_code   VARCHAR(7),
        birth_date    DATE,
        salary        NUMERIC(7, 2),
        parking_spot  NUMERIC(4),
        gender        CHAR,
        department_id NUMERIC(2),
        manager_id    CHAR(9),
        CONSTRAINT pk_employees PRIMARY KEY (employee_id)
    );
    """
    cursor.execute(create_table_query)
    conn.commit()

    # Insert data into employees table
    insert_data_query = """
    INSERT INTO employees
        (employee_id, last_name, first_name, infix, street, location, province, postal_code, birth_date, salary, parking_spot, gender, department_id, manager_id)
    VALUES
        ('999666666', 'Bordoloi', 'Bijoy', '', 'Zuidelijke Rondweg 12', 'Eindhoven', 'NB', '6202 EK', '1977-11-10', 55000.00, 1, 'M', 1, NULL),
        ('999555555', 'Jochems', 'Suzan', '', 'Nuthseweg 17', 'Maastricht', 'LI', '9394 LR', '1981-06-20', 43000.00, 3, 'F', 3, '999666666'),
        ('999444444', 'Zuiderweg', 'Willem', '', 'Lindberghdreef 303', 'Oegstgeest', 'ZH', '2340 RV', '1985-08-12', 43000.00, 32, 'M', 7, '999666666'),
        ('999887777', 'Muiden', 'Martina', 'van der', 'Hoofdstraat 14', 'Maarssen', 'UT', '9394 LM', '1988-07-19', 25000.00, 402, 'F', 3, '999555555'),
        ('999222222', 'Amelsvoort', 'Henk', 'van', 'Zeestraat 14', 'Maastricht', 'LI', '9394 MK', '1979-03-29', 25000.00, 422, 'M', 3, '999555555'),
        ('999111111', 'Bock', 'Douglas', '', 'Monteverdidreef 2', 'Oegstgeest', 'ZH', '6312 CB', '1965-09-01', 30000.00, 542, 'M', 7, '999444444'),
        ('999333333', 'Joosten', 'Dennis', '', 'Eikenstraat 10', 'Groningen', 'GR', '6623 HK', '1982-09-15', 38000.00, 332, 'M', 7, '999444444'),
        ('999888888', 'Pregers', 'Shanya', '', 'Overtoomweg 44', 'Eindhoven', 'NB', '6202 MR', '1982-07-31', 25000.00, 296, 'F', 7, '999444444'),
        ('900000009', 'Johnson', 'Dan', 'Leo', 'Grotesteenweg 23', 'Berchem', 'BE', '2600 BE', '1992-10-09', 45000.00, 23, 'M', 7, '999666666'),
        ('123456789', 'Smith', 'John', 'J', '123 Main St', 'Toronto', 'ON', 'M1A 1A1', '1990-01-01', 20000.00, 40, 'M', 3, '999666666'),
        ('987654321', 'Johnson', 'Jane', 'J', '456 Elm St', 'Toronto', 'ON', 'M2A 2A2', '1995-01-01', 24000.00, 41, 'F', 7, '999555555'),
        ('111111111', 'Davis', 'David', 'D', '789 Oak St', 'Toronto', 'ON', 'M3A 3A3', '1992-01-01', 25000.00, 42, 'M', 3, '999666666'),
        ('222222222', 'Harris', 'Helen', 'H', '901 Maple St', 'Toronto', 'ON', 'M4A 4A4', '1998-01-01', 38000.00, 43, 'F', 3, '999555555'),
        ('333333333', 'Martin', 'Michael', 'M', '1111 Pine St', 'Toronto', 'ON', 'M5A 5A5', '1991-01-01', 29000.00, 44, 'M', 7, '999666666'),
        ('444444444', 'Taylor', 'Tina', 'T', '2222 Spruce St', 'Toronto', 'ON', 'M6A 6A6', '1996-01-01', 34000.00, 45, 'F', 7, '999666666'),
        ('555555555', 'Walker', 'William', 'W', '3333 Cedar St', 'Toronto', 'ON', 'M7A 7A7', '1993-01-01', 41000.00, 46, 'M', 3, '999666666'),
        ('666666666', 'Brown', 'Brenda', 'B', '4444 Willow St', 'Toronto', 'ON', 'M8A 8A8', '1994-01-01', 30000.00, 47, 'F', 3, '999666666');
    """
    cursor.execute(insert_data_query)
    conn.commit()

    cursor.close()
    conn.close()

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
    # Attempt to create tables if they don't exist
    try:
        create_tables()
    except Exception as e:
        print(f"Error creating tables: {e}")

    # Run Flask app
    app.run(host='0.0.0.0', port=8080, debug=True)







# import psycopg2
# import os
# from flask import Flask, jsonify
# from decimal import Decimal
# from dotenv import load_dotenv
# import time
#
# load_dotenv()
#
# app = Flask(__name__)
#
# # Database connection setup
# DB_NAME = os.getenv('POSTGRES_DB', 'Enterprise')
# DB_USER = os.getenv('POSTGRES_USER', 'postgres')
# DB_PASS = os.getenv('POSTGRES_PASSWORD', 'Student_1234')
# DB_PORT = os.getenv('POSTGRES_PORT', '5432')
# DB_HOST = 'postgres'  # Ensure this matches the service name in docker-compose.yml
#
# def get_db_connection(retries=5):
#     attempts = 0
#     while attempts < retries:
#         try:
#             conn = psycopg2.connect(
#                 dbname=DB_NAME,
#                 user=DB_USER,
#                 password=DB_PASS,
#                 host=DB_HOST,
#                 port=DB_PORT
#             )
#             return conn
#         except psycopg2.OperationalError as e:
#             print(f"Connection attempt {attempts + 1} failed: {e}")
#             attempts += 1
#             time.sleep(2)  # Wait for 2 seconds before retrying
#
#     raise Exception(f"Failed to connect to database after {retries} attempts.")
#
# def create_tables():
#     conn = get_db_connection()
#     cursor = conn.cursor()
#
#     # Example: Create 'employees' table
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS employees (
#             id SERIAL PRIMARY KEY,
#             name VARCHAR(100),
#             age INT
#         )
#     ''')
#
#     conn.commit()
#     cursor.close()
#     conn.close()
#
# def convert_decimal(data):
#     if isinstance(data, list):
#         return [convert_decimal(item) for item in data]
#     elif isinstance(data, tuple):
#         return tuple(convert_decimal(item) for item in data)
#     elif isinstance(data, dict):
#         return {key: convert_decimal(value) for key, value in data.items()}
#     elif isinstance(data, Decimal):
#         return float(data)
#     else:
#         return data
#
# @app.route('/')
# def index():
#     return "Welcome to the Flask PostgreSQL app!"
#
# # Fetch all employees
# @app.route('/employees', methods=['GET'])
# def get_employees():
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM employees;')
#     employees = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     employees = convert_decimal(employees)  # Convert Decimal types to float
#     return jsonify(employees)
#
# if __name__ == '__main__':
#     # Attempt to create tables if they don't exist
#     try:
#         create_tables()
#     except Exception as e:
#         print(f"Error creating tables: {e}")
#
#     # Run Flask app
#     app.run(host='0.0.0.0', port=8080, debug=True)
#
#
#
#





# import psycopg2
# import os
# from flask import Flask, jsonify
# from decimal import Decimal
# from dotenv import load_dotenv
#
# load_dotenv()
#
# app = Flask(__name__)
#
# # Database connection setup
# DB_NAME = os.getenv('POSTGRES_DB', 'Enterprise')
# DB_USER = os.getenv('POSTGRES_USER', 'postgres')
# DB_PASS = os.getenv('POSTGRES_PASSWORD', 'Student_1234')
# DB_PORT = os.getenv('POSTGRES_PORT', '5432')
# DB_HOST = 'postgres'
#
# def get_db_connection():
#     conn = psycopg2.connect(
#         dbname=DB_NAME,
#         user=DB_USER,
#         password=DB_PASS,
#         host=DB_HOST,
#         port=DB_PORT
#     )
#     return conn
#
# def create_tables():
#     conn = get_db_connection()
#     cursor = conn.cursor()
#
#     # Example: Create 'employees' table
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS employees (
#             id SERIAL PRIMARY KEY,
#             name VARCHAR(100),
#             age INT
#         )
#     ''')
#
#     conn.commit()
#     cursor.close()
#     conn.close()
#
# def convert_decimal(data):
#     if isinstance(data, list):
#         return [convert_decimal(item) for item in data]
#     elif isinstance(data, tuple):
#         return tuple(convert_decimal(item) for item in data)
#     elif isinstance(data, dict):
#         return {key: convert_decimal(value) for key, value in data.items()}
#     elif isinstance(data, Decimal):
#         return float(data)
#     else:
#         return data
#
# @app.route('/')
# def index():
#     return "Welcome to the Flask PostgreSQL app!"
#
# # Fetch all employees
# @app.route('/employees', methods=['GET'])
# def get_employees():
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM employees;')
#     employees = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     employees = convert_decimal(employees)  # Convert Decimal types to float
#     return jsonify(employees)
#
# if __name__ == '__main__':
#     # Create tables if they don't exist
#     create_tables()
#
#     # Run Flask app
#     app.run(host='0.0.0.0', port=8080, debug=True)
#



# from flask import Flask, request, jsonify
# import psycopg2
# import os
# from decimal import Decimal
# from dotenv import load_dotenv
#
# load_dotenv()
#
# app = Flask(__name__)
#
# # Database connection setup
# DB_NAME = os.getenv('POSTGRES_DB', 'Enterprise')
# DB_USER = os.getenv('POSTGRES_USER', 'postgres')
# DB_PASS = os.getenv('POSTGRES_PASSWORD', 'Student_1234')
# DB_PORT = os.getenv('POSTGRES_PORT', '5432')
# DB_HOST = 'db'
#
# # # Check if running within Docker container
# # DOCKER_CONTAINER = os.getenv('DOCKER_CONTAINER')
# #
# # if DOCKER_CONTAINER:
# #     # Running within Docker container, use 'postgres' as hostname
# #     DB_HOST = 'postgres'
# # else:
# #     # Running locally, use 'localhost' as hostname
# #     DB_HOST = 'localhost'
#
# def get_db_connection():
#     conn = psycopg2.connect(
#         dbname=DB_NAME,
#         user=DB_USER,
#         password=DB_PASS,
#         host=DB_HOST,
#         port=DB_PORT
#     )
#     return conn
#
# def convert_decimal(data):
#     if isinstance(data, list):
#         return [convert_decimal(item) for item in data]
#     elif isinstance(data, tuple):
#         return tuple(convert_decimal(item) for item in data)
#     elif isinstance(data, dict):
#         return {key: convert_decimal(value) for key, value in data.items()}
#     elif isinstance(data, Decimal):
#         return float(data)
#     else:
#         return data
#
# @app.route('/')
# def index():
#     return "Welcome to the Flask PostgreSQL app!"
#
# # Fetch all employees
# @app.route('/employees', methods=['GET'])
# def get_employees():
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM employees;')
#     employees = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     employees = convert_decimal(employees)  # Convert Decimal types to float
#     return jsonify(employees)
#
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080, debug=True)
#     # app.run(port=8080, debug=True)
#     # Path to SSL/TLS certificate and private key
#     # ssl_cert = os.path.join(os.path.dirname(__file__), '.\src\certs\server.crt')
#     # ssl_key = os.path.join(os.path.dirname(__file__), '.\src\certs\server.key')
#     #
#     # # Run Flask app with SSL/TLS
#     # app.run(host='0.0.0.0', port=5000, ssl_context=(ssl_cert, ssl_key))
#     # app.run(host='0.0.0.0', port=8080, ssl_context=(ssl_cert, ssl_key))