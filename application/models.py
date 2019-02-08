from application import db

class Product(db.Model):
   
    __abstract__= True

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    price = db.Column(db.String(20), nullable=False)
