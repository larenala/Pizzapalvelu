from application import app, db
from flask import redirect, render_template, request, url_for
from application.orders.models import Tilaus

@app.route("/orders/", methods=["GET"])
def orders_index():
    return render_template("orders/list.html", orders=Tilaus.query.all())

@app.route("/orders/<order_id>/", methods=["POST"])
def orders_set_delivered(order_id):
    t=Tilaus.query.get(order_id)
    t.done=True
    db.session().commit()

    return redirect(url_for("orders_index"))

@app.route("/orders/new/")
def orders_form():
    return render_template("orders/new.html")

@app.route("/orders/", methods=["POST"])
def orders_create():
    t = Tilaus(request.form.get("name"))
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("orders_index"))
