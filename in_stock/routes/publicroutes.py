from flask import render_template, url_for, request, redirect
from in_stock import app, db, login_manager



@app.route("/")
def index():
	return render_template("index.html")



@app.route("/login")
def login():
	return render_template("login.html")



@app.route("/register")
def register():
	return render_template("register.html")