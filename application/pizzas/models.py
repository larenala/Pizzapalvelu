from application import db

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    onupdate=db.func.current_timestamp()
    ingredient = db.Column(db.String(144), nullable=False)
    name = db.Column(db.String(144), nullable=False)

    def __init__(self, name, ingredient):
        self.name = name
        self.ingredient = ingredient
