from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import AccountForm, LoginForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")


    login_user(user)
    return redirect(url_for("index"))    

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))    

@app.route("/auth/new/")
def users_form():
    return render_template("auth/new.html", form=AccountForm())

@app.route("/auth/new", methods=["POST"])
def create_user():
    form = AccountForm(request.form)
    if not form.validate():
      return render_template("auth/new.html", form=form)

    name=form.name.data
    username =form.username.data
    password = form.password.data
    user = User(name, username, password)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))