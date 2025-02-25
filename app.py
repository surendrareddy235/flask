from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def showapp():
    return render_template("app.html")

@app.route("/formpage", methods=["post"])
def showformpage():
    name = request.form.get("name")
    email = request.form.get("email")
    return render_template("success.html",name=name,email=email)

if __name__ == "__main__":
    app.run(debug=True)