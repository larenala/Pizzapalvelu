from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username", [validators.InputRequired])
    password = PasswordField("Password", [validators.InputRequired("Please enter your password.")])
  
    class Meta:
        csrf = False

class AccountForm(FlaskForm):
     name = StringField("Name", [validators.InputRequired("Please enter your name.")])
     username = StringField("Username", [validators.Length(min=2, max=25)])
     password = PasswordField("Password", [validators.Length(min=8, max=25)])
     password = PasswordField('New Password', [
         validators.DataRequired(),
         validators.EqualTo('confirm', message='Passwords must match')
     ])
     confirm = PasswordField('Repeat Password')

     class Meta:
         csrf = False
