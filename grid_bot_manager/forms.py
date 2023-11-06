## forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=64)])
    password = PasswordField('Password', validators=[DataRequired()])

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])

class BotCreationForm(FlaskForm):
    exchange = StringField('Exchange', validators=[DataRequired(), Length(max=64)])
    symbol = StringField('Symbol', validators=[DataRequired(), Length(max=64)])
    lower_price = FloatField('Lower Price', validators=[DataRequired()])
    upper_price = FloatField('Upper Price', validators=[DataRequired()])
    grid_levels = IntegerField('Grid Levels', validators=[DataRequired()])
