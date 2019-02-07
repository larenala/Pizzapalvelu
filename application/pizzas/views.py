from application import app, db

from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application.pizzas.models import Pizza
from application.pizzas.forms import PizzaForm

@app.route("/pizzas", methods=["GET"])
def pizzas_index():
   return render_template("pizzas/list.html", pizzas=Pizza.query.all()) 

@app.route("/pizzas/<pizza_id>/", methods=["GET"])
def show_pizza(pizza_id):    
    return render_template("pizzas/pizza.html", pizza=Pizza.query.filter_by(id=pizza_id).first())

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
    price = form.price.data
    p = Pizza(name, ingredients, img, price)
    db.session().add(p)
    db.session().commit()  
    return redirect(url_for('pizzas_index'))

@app.route("/pizzas/edit/<pizza_id>/", methods=["GET"])
def pizza_edit_index(pizza_id):
    return render_template("pizzas/edit.html", pizza=Pizza.query.get(pizza_id), form=PizzaForm())

@app.route("/pizzas/edit/<pizza_id>/", methods=["POST"])
def pizza_update(pizza_id):
    p=Pizza.query.get(pizza_id)
    form=PizzaForm(request.form)

    if form.name.data:
          p.name=form.name.data
    p.ingredients=form.ingredients.data
    p.img = form.img.data
    p.price = form.price.data
    db.session().commit()
    return redirect(url_for('pizzas_index'))

@app.route("/pizzas/delete/<pizza_id>/", methods=["POST"])
@login_required
def pizza_delete(pizza_id):
    p=Pizza.query.get(pizza_id)
    db.session().delete(p)
    db.session().commit()
    return redirect(url_for('pizzas_index'))


