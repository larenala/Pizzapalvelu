from application import app, db

from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application.pizzas.models import Pizza
from application.pizzas.forms import PizzaForm

@app.route("/pizzas", methods=["GET"])
def pizzas_index():
   return render_template("pizzas/list.html", pizzas=Pizza.query.all()) 

@app.route("/pizzas/new/")
@login_required
def pizzas_form():
    return render_template("pizzas/new.html", form=PizzaForm())

@app.route("/pizzas/", methods=["POST"])
@login_required
def pizza_create():
    form = PizzaForm(request.form)

    if not form.validate():
        return render_template("pizzas/new.html", form = form)

    name = form.name.data
    ingredients = form.ingredients.data
    img = form.img.data
    p = Pizza(name, ingredients, img)
    db.session().add(p)
    db.session().commit()  
    return redirect(url_for('pizzas_index'))
