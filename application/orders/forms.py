from flask_wtf import FlaskForm
from wtforms import StringField

class OrderForm(FlaskForm):
    name = StringField("Name")
    address = StringField("Delivery address")
    phone = StringField("Phone number")

    class Meta:
        csrf = False
