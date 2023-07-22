from flask import render_template, url_for, request, redirect

from in_stock import app, db, login_manager

@app.route("/homepage") # groupname/pantry
@login_required
def homepage():
	return render_template("auth/homepage.html")