from flask_wtf import FlaskForm
from wtforms import StringField, validators

class PizzaForm(FlaskForm):
    name = StringField("Name ", [
        validators.InputRequired("Please enter the name of the pizza."),
        validators.Length(min=4, max=30)])
    ingredients = StringField("Ingredients ", [
        validators.InputRequired("Please enter the ingredients."),
        validators.Length(min=2, max=100)])    
    img = StringField("Link to image ", [
        validators.InputRequired("Please enter a valid url for image."),
        validators.URL(require_tld=False, message="Please enter a valid url")]) 
    price = StringField("Price ", [
        validators.InputRequired("Please enter a price."),
        validators.Length(min=1, max=6)]) 

    class Meta:
        csrf = False
