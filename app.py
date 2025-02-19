from flask import Flask, render_template, request,redirect,url_for

app = Flask(__name__)
@app.route("/")
def showindex():
    return render_template('index.html')

@app.route("/successform",methods = ["POST"])
def show_submitform():
    name = request.form.get('name')
    email = request.form.get('email')
    gender = request.form.get('gender')
    return render_template('successform.html',name = name,email = email,gender = gender)

if __name__ == "__main__":
    app.run(debug=True)