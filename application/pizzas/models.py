from application import db
from application.models import Product

from sqlalchemy.sql import text

class Pizza(Product):

    __tablename__ = "pizza"

    id = db.Column(db.Integer, primary_key=True)
    ingredients = db.Column(db.String(144), nullable=False)
    img = db.Column(db.String(200), nullable=False) 
    available = db.Column(db.Boolean, default=True)
    ordered_pizzas = db.relationship("OrderPizza", backref='pizza', lazy=True)

    def __init__(self, name, ingredients, img, price):
        self.name = name
        self.ingredients = ingredients
        self.img = img
        self.price = price

    @staticmethod
    def show_pizza_stats():    
        pizzas=Pizza.query.all()
        stmt=text("SELECT Pizza.name, COUNT(order_pizza.id) AS sold FROM order_pizza"
                  " LEFT JOIN pizza ON order_pizza.pizza_id=pizza.id GROUP BY pizza.name ORDER BY pizza.name ASC") 
        res = db.engine.execute(stmt)       
        response = []
        for row in res:
            response.append({"name":row[0], "sold":row[1] })
        return response