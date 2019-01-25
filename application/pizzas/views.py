from application import app, db
from flask import redirect, render_template, request, url_for
from application.pizzas.models import Pizza

@app.route("/pizzas", methods=["GET"])
def pizzas_index():
   return render_template("pizzas/list.html", pizzas=Pizza.query.all()) 

@app.route("/pizzas/new/")
def pizzas_form():
    return render_template("pizzas/new.html")

@app.route("/pizzas/", methods=["POST"])
def pizza_create():
    name = request.form.get("name")
    ingredient = request.form.get("ingredient")
    p = Pizza(name, ingredient)
    db.session().add(p)
    db.session().commit()  
    return redirect(url_for('pizzas_index'))
