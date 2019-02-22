from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required

from application.pizzas.models import Pizza
from application.pizzas.forms import PizzaForm
from application.orders.models import Tilaus, OrderPizza
from application.auth.models import User

@app.route("/pizzas", methods=["GET"])
def pizzas_index():
   return render_template("pizzas/list.html", pizzas=Pizza.query.filter_by(available=True)) 

@app.route("/pizzas/<pizza_id>/", methods=["GET"])
def show_pizza(pizza_id):    
    return render_template("pizzas/pizza.html", pizza=Pizza.query.filter_by(id=pizza_id).first())

@app.route("/pizzas/order/<pizza_id>/", methods=["GET", "POST"])
@login_required(role="USER")
def add_to_order(pizza_id):
    id = current_user.get_id()
    if request.method == "GET":
        return render_template("orders/myorders.html", orders=Tilaus.query.filter_by(account_id=id))
    user = User.query.get(id)

    if user.current_order == False:
        user.current_order = True
        pizza = Pizza.query.get(pizza_id)
        order = Tilaus(id, pizza.price)
        db.session.add(order)
        db.session.commit()
        ind = order.id
        tilausPizza = OrderPizza(ind, pizza_id)
        db.session.add(tilausPizza)
        db.session.commit()
        
    else:
        orders = Tilaus.query.filter_by(account_id=id)
        len = orders.count()
        if (len == 0): 
            len=1
        o = orders[len-1]
        tilausPizza = OrderPizza(o.id, pizza_id)
        pizza = Pizza.query.filter_by(id=pizza_id).one()
        o.price += float(pizza.price)
        db.session.add(tilausPizza)
        db.session.commit()
    return redirect(url_for('pizzas_index'))

@app.route("/pizzas/new/")
@login_required(role="ADMIN")
def pizzas_form():
    return render_template("pizzas/new.html", form=PizzaForm())

@app.route("/pizzas/", methods=["POST"])
@login_required(role="ADMIN")
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

@app.route("/pizzas/edit", methods=["GET"]) 
@login_required (role="ADMIN")
def pizza_edit_page():
    return render_template("pizzas/editlist.html", pizzas=Pizza.query.filter_by(available=True))

@app.route("/pizzas/edit/<pizza_id>/", methods=["GET", "POST"])
@login_required(role="ADMIN")
def pizza_update(pizza_id):
    if request.method == "GET":
        return render_template("pizzas/edit.html", pizza=Pizza.query.get(pizza_id), form=PizzaForm())

    p=Pizza.query.get(pizza_id)
    form=PizzaForm(request.form)

    if form.name.data:
          p.name=form.name.data
    p.ingredients=form.ingredients.data
    p.img = form.img.data
    p.price = form.price.data
    db.session().commit()
    return redirect(url_for('pizza_edit_page'))


@app.route("/pizzas/delete/<pizza_id>/", methods=["POST"])
@login_required(role="ADMIN")
def pizza_delete(pizza_id):
    p=Pizza.query.get(pizza_id)
    p.available=False
    db.session().commit()
    return redirect(url_for('pizzas_index'))


