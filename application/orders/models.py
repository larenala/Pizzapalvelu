from application import db

class Tilaus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    delivery_date = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())
    name = db.Column(db.String(144))
    address = db.Column(db.String(144))
    phone = db.Column(db.String(15))
    delivered = db.Column(db.Boolean, nullable=False)
    price = db.Column(db.String(20), nullable=False)

    account_id=db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, account_id, price=0):
        self.account_id = account_id
        self.delivered = False
        self.price = price
