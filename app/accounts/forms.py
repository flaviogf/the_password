from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class CreateAccountForm(FlaskForm):
    name = StringField('Name',
                       validators=[DataRequired()])
    login = StringField('Login',
                        validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    submit = SubmitField('Save')
