from application import db
from application.pizzas.models import Pizza
from flask_login import current_user


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
    price = db.Column(db.Float(10), nullable=False)
    items = db.Column(db.String(100))
    sent = db.Column(db.Boolean, nullable=False)
    orderedPizzas=db.relationship("OrderPizza", backref='order', lazy=True)

    account_id=db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    

    def __init__(self, account_id, price=0):
        self.account_id = account_id
        self.delivered = False
        self.price = price 
        self.items = ""
        self.sent = False

    @staticmethod
    def find_pizzas_for_order(order_id):
        user_id=current_user.get_id()
        order_id = str(order_id)
        stmt=text("SELECT Pizza.name, Pizza.price, Order_pizza.order_id FROM Pizza, Order_pizza"
                  " WHERE Order_pizza.order_id == :orderid AND Order_pizza.pizza_id == Pizza.id").params(orderid= order_id)
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"name":row[0], "price":row[1]})

        return response


class OrderPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id=db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    pizza_id=db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)

    def __init__(self, order_id, pizza_id):
        self.order_id = order_id    
        self.pizza_id = pizza_id

    @staticmethod
    def find_pizzas_for_order(order_id):
        user_id = current_user.get_id()
        stmt=text("SELECT Pizza.id, Pizza.name, Pizza.price, Account.id, Tilaus.id, Order.sent FROM Pizza, Account, Tilaus"
                    " LEFT JOIN OrderPizza ON OrderPizza.pizza_id = Pizza.id, OrderPizza.account_id=Account.id"
                    " WHERE (Order.sent IS = 1)"
                    " GROUP BY Pizza.name")
        res=db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name": row[0]})
  
        return response

