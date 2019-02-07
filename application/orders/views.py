
from application import app, db
from flask import redirect, render_template, request, url_for
from application.orders.models import Tilaus
from application.orders.forms import OrderForm
from application.auth.models import User
from flask_login import login_required, current_user

@app.route("/orders/", methods=["GET"])
def orders_index():
    return render_template("orders/list.html", orders=Tilaus.query.all())

@app.route("/orders/<order_id>/", methods=["POST"])
def orders_set_delivered(order_id):
    t=Tilaus.query.get(order_id)
    t.delivered=True
    db.session().commit()

    return redirect(url_for("orders_index"))

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
    price=10
    t = Tilaus(id, price)
    t.name=form.name.data
    t.address=form.address.data
    t.phone = form.phone.data
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("orders_index"))
