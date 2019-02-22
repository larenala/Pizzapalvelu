from application import db
from application.models import Product

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

    
