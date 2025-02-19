from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def connect_to_database():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "19030ee235",
        database = "school"
    )
def create_table():
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS flask_db(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),  
            email VARCHAR(100),
            password VARCHAR(100),
            mobile INTEGER           
        )
        """)
        connection.commit()
        cursor.close()
        connection.close()
        print("Table created successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def insert_data(name,email,password,mobile):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO flask_db (name,email,password,mobile)
    VALUES(%s, %s, %s, %s)
    """, (name,email,password,mobile))
    connection.commit()
    cursor.close()
    connection.close()
@app.route("/")
def showindex():
    return render_template("index.html")

@app.route("/successform",methods=["POST"])
def showformpage():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    mobile = request.form["mobile"]
    insert_data(name,email,password,mobile)
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("select* from flask_db")
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template("successform.html",users = users)

if __name__ == "__main__":
    create_table()
    app.run(debug=True)
