from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'hrms.db'

# Helper function to establish database connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# API endpoints for managing employees
@app.route('/employees', methods=['GET'])
def get_employees():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    conn.close()
    return jsonify([dict(row) for row in employees])

@app.route('/employees', methods=['POST'])
def add_employee():
    # Code for adding employee
    pass

@app.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    # Code for updating employee
    pass

@app.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    # Code for deleting employee
    pass

# Similarly, endpoints can be created for managing departments and performance reviews

if __name__ == '__main__':
    app.run(debug=True)
