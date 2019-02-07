from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class AccountForm(FlaskForm):
     name = StringField("Name")
     username = StringField("Username")
     password = PasswordField("Password", [validators.Length(min=8, max=25)])

     class Meta:
         csrf = False
