from flask_wtf import FlaskForm
from wtforms import StringField, validators

class OrderForm(FlaskForm):
    name = StringField("Name", [
        validators.InputRequired("Please enter a name."),
        validators.Length(min=4, max=35)])
    address = StringField("Delivery address", [
        validators.InputRequired("Please enter a delivery address."),
        validators.Length(min=4, max=80)])
    phone = StringField("Phone number", [
        validators.InputRequired("Please enter a phonenumber."),
        validators.Length(min=6, max=15)])

    class Meta:
        csrf = False
