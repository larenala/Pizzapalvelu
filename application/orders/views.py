
from application import app, db
from flask import redirect, render_template, request, url_for
from application.orders.models import Tilaus, OrderPizza
from application.orders.forms import OrderForm
from application.pizzas.models import Pizza
from application.auth.models import User

from flask_login import login_required, current_user

@app.route("/orders/", methods=["GET"])
def orders_index():
    return render_template("orders/list.html", orders=Tilaus.query.filter_by(sent=True))


@app.route("/myorders/", methods=["GET"])
def myorders_index():
    id = current_user.get_id()
    return render_template("orders/myorders.html", orders=Tilaus.query.filter_by(account_id=id, sent=True))

@app.route("/orders/<order_id>/", methods=["POST"])
def orders_set_delivered(order_id):
    t=Tilaus.query.get(order_id)
    t.delivered=True
    db.session().commit()

    return redirect(url_for("orders_index"))

@app.route("/orders/send/", methods=["GET"])
@login_required
def send_order_main():
    user_id = current_user.get_id()
    user=User.query.get(user_id)
    if user.current_order == False:
        return render_template("orders/order.html")
    orders = Tilaus.query.filter_by(account_id=user_id)
    len = orders.count()
    if len == 0:
        len=1
    order = orders[len-1]

    id=order.id
    orderPizzas = OrderPizza.query.filter_by(order_id=id)
    pizzalist = [] 
    p = OrderPizza.find_pizzas()

    for item in orderPizzas:
        p_id = item.pizza_id
        pizza = Pizza.query.get(p_id)
        pizzalist.append(pizza)
    return render_template("orders/new.html", order = order, pizzas=pizzalist, form=OrderForm())

@app.route("/orders/send/<order_id>/", methods=["GET", "POST"])
@login_required
def send_order(order_id):
    if request.method == 'GET':
        return render_template("orders/myorders.html", orders=Tilaus.query.filter_by(account_id=current_user.get_id()))
    order = Tilaus.query.get(order_id)
    form = OrderForm(request.form)
    order.name = form.name.data
    order.address = form.address.data
    order.phone = form.phone.data
    order.sent = True
    user_id = current_user.get_id()
    user = User.query.get(user_id)
    user.current_order = False
    db.session.commit()
    return redirect(url_for('myorders_index'))