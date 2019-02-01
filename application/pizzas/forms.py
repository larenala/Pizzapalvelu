from flask_wtf import FlaskForm
from wtforms import StringField, validators

class PizzaForm(FlaskForm):
    name = StringField("Name ", [validators.Length(min=4, max=30)])
    ingredients = StringField("Ingredients ", [validators.Length(min=2, max=100)])    
    img = StringField("Link to image ", [validators.URL(require_tld=False, message=None)]) 
    price = StringField("Price ", [validators.Length(min=2, max=6)]) 

    class Meta:
        csrf = False
