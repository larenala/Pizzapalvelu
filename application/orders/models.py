from application import db

from sqlalchemy.sql import text

class Tilaus(db.Model):

    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    delivery_date = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())
    name = db.Column(db.String(144))
    address = db.Column(db.String(144))
    phone = db.Column(db.String(15))
    delivered = db.Column(db.Boolean, nullable=False)
    price = db.Column(db.String(20), nullable=False)
    items = db.Column(db.String(100))

    orderedPizzas=db.relationship("OrderPizza", backref='order', lazy=True)

    account_id=db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    

    def __init__(self, account_id, price=0):
        self.account_id = account_id
        self.delivered = False
        self.price = price 
        self.items = ""


class OrderPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id=db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    pizza_id=db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)

    def __init__(self, order_id, pizza_id):
        self.order_id = order_id    
        self.pizza_id = pizza_id

    @staticmethod
    def find_pizza():
        stmt=text("SELECT pizza.id, pizza.name, pizza.price FROM Pizza, OrderPizza WHERE pizza.id=OrderPizza.pizza_id")
        res=db.engine.execute(stmt)

        for row in res:
            print(row[0])
