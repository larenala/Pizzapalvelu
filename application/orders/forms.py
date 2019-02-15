from flask_wtf import FlaskForm
from wtforms import StringField, validators

class OrderForm(FlaskForm):
    items = StringField("Ordered items ")
    name = StringField("Name", [validators.Length(min=4, max=35)])
    address = StringField("Delivery address", [validators.Length(min=4, max=50)])
    phone = StringField("Phone number", [validators.Length(min=6, max=15)])

    class Meta:
        csrf = False
