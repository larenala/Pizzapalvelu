from application import db

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    onupdate=db.func.current_timestamp()
    ingredients = db.Column(db.String(144), nullable=False)
    name = db.Column(db.String(144), nullable=False)
    img = db.Column(db.String(200), nullable=False)

    def __init__(self, name, ingredients, img):
        self.name = name
        self.ingredients = ingredients
        self.img = img
