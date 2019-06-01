from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/codwithpiyush'


app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login/index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard/index.html")

app.run(debug=True)