from application import db

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    ingredients = db.Column(db.String(144), nullable=False)
    img = db.Column(db.String(200), nullable=False)
    price = db.Column(db.String(100), nullable=False)

    def __init__(self, name, ingredients, img, price):
        self.name = name
        self.ingredients = ingredients
        self.img = img
        self.price = price
