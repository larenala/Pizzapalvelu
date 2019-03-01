from flask import flash, render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db, login_required

from application.orders.models import Tilaus, OrderPizza
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
        flash('The username or password does not exist')
        return render_template("auth/loginform.html", form = form)
    login_user(user)
    flash('You were successfully logged in')
    return redirect(url_for('pizzas_index'))

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
    role = "USER"
    user = User(name, username, password, role)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('auth_login'))

@app.route ("/auth/list", methods=["GET"])
@login_required(role='ADMIN')
def list_users():
    per_page=8
    page = request.args.get('page', 1, type=int)
    accounts=User.query.paginate(page, per_page, False)
    next_url = url_for('list_users', page=accounts.next_num) \
        if accounts.has_next else None
    prev_url = url_for('list_users', page=accounts.prev_num) \
        if accounts.has_prev else None
    return render_template("auth/list.html", accounts=accounts.items, page=1, next_url=next_url, prev_url=prev_url)

@app.route("/auth/stats", methods=["GET"])
@login_required(role='ADMIN')
def customers_stats_index():
    return render_template("auth/customerstats.html", accountaverages=User.show_account_stats())    


@app.route("/auth/<user_id>", methods=["POST"])
def user_disable_orders(user_id):
    user = User.query.get(user_id)
    user.blacklist = True
    db.session().commit()

    return redirect(url_for("list_users"))

@app.route("/auth/delete/<user_id>", methods=["GET", "POST"])
def user_delete(user_id):
    user = User.query.get(user_id)
    orders = Tilaus.query.filter_by(account_id=user.id)
    for order in orders:
        orderpizzas = OrderPizza.query.filter_by(order_id=order.id)
        for orderpizza in orderpizzas:
            db.session.delete(orderpizza)
        db.session.delete(order)    
    db.session.delete(user)    
    db.session().commit()
    flash('Account and all related orders were removed from the database.')
    return redirect(url_for("list_users"))    


