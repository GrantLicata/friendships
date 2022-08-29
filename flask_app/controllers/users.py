from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.user import User
from pprint import pprint

@app.route("/")
def index():
    users_list = User.get_all()
    friends_list = User.get_friendships()
    pprint(friends_list, width=1)
    return render_template("index.html", friends = friends_list, users = users_list)

@app.route('/add_user', methods=["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
    }
    User.add_user(data)
    return redirect('/')

@app.route('/add_friendship', methods=["POST"])
def create_friendship():
    data = {
        "user_id": request.form["user"],
        "friend_id" : request.form["friend"],
    }
    User.create_friendship(data)
    return redirect('/')
