from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class SearchForm(FlaskForm):
    #search = TextAreaField('Search', validators=[length(max=200)])
    search = StringField('Search', validators=[length(max=200)])
    submit = SubmitField('search')
