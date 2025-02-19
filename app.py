from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database setup: creating the table if it doesn't exist
def init_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        email TEXT,
                        gender TEXT,
                        mobile TEXT)''')
    conn.commit()
    conn.close()

# Route to show the form
@app.route("/")
def showindex():
    return render_template('index.html')

# Route to handle the form submission and store the data in SQLite
@app.route("/successform", methods=["POST"])
def show_submitform():
    name = request.form.get('name')
    email = request.form.get('email')
    gender = request.form.get('gender')
    mobile = request.form.get('mobile')

    # Insert data into the database
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO users (name, email, gender, mobile) 
                      VALUES (?, ?, ?, ?)''', (name, email, gender, mobile))
    conn.commit()
    conn.close()

    # Fetch all data to show in a table format
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()

    return render_template('successform.html', users=users)

if __name__ == "__main__":
    init_db()  # Initialize the database and table
    app.run(debug=True)
