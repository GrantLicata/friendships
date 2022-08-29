from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.user import User

@app.route("/")
def index():
    friends_list = User.get_friendships()
    return render_template("index.html", friends = friends_list)

@app.route('/add_user', methods=["POST"])
def create():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
    }
    User.add_user(data)
    return redirect('/')
