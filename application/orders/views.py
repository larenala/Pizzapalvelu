
from application import app, db
from flask import redirect, render_template, request, url_for
from application.orders.models import Tilaus, OrderPizza
from application.orders.forms import OrderForm
from application.pizzas.models import Pizza
from application.auth.models import User

from flask_login import login_required, current_user

@app.route("/orders/", methods=["GET"])
def orders_index():
    return render_template("orders/list.html", orders=Tilaus.query.all())


@app.route("/myorders/", methods=["GET"])
def myorders_index():
    id = current_user.get_id()
    return render_template("orders/myorders.html", orders=Tilaus.query.filter_by(account_id=id))

@app.route("/orders/<order_id>/", methods=["POST"])
def orders_set_delivered(order_id):
    t=Tilaus.query.get(order_id)
    t.delivered=True
    db.session().commit()

    return redirect(url_for("orders_index"))

@app.route("/orders/<order_id>", methods=["GET"])
@login_required
def show_order(order_id):
    id=order_id
    orderPizzas = OrderPizza.query.filter_by(order_id=id)
    pizzalist = [] 
    for item in orderPizzas:
        p_id = item.pizza_id
        pizza = Pizza.query.get(p_id)
        pizzalist.append(pizza)
    return render_template("orders/new.html", form=OrderForm(),  pizzas = pizzalist, order=Tilaus.query.filter_by(id=order_id).first())

@app.route("/orders/new/")
@login_required
def orders_form():
    id = current_user.get_id()
    user=User.query.get(id)
    return render_template("orders/new.html", form=OrderForm(), user=user)


@app.route("/orders/", methods=["POST"])
@login_required
def orders_send():
    form=OrderForm(request.form)
    if not form.validate():
        return render_template("orders/new.html", form=form)

    id = current_user.get_id()
    user = user.get_by_id(id)
    orders = Tilaus.query.filter_by(account_id=id).count()
    len = orders.count()
    order = orders[len]    
    order.price=order.price
    order.username=form.name.data
    order.address=form.address.data
    order.phone = form.phone.data
    user.current_order = False
    db.session().add(order)
    db.session().commit()

    return redirect(url_for("myorders_index"))
