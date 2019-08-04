from flask_wtf import FlaskForm
from wtforms import (BooleanField, FileField, PasswordField, StringField,
                     SubmitField)
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = EmailField('E-mail',
                       validators=[DataRequired(),
                                   Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember', default=True)
    submit = SubmitField('Login')


class ProfileForm(FlaskForm):
    name = StringField('Name',
                       validators=[DataRequired()])
    email = EmailField('E-mail',
                       validators=[DataRequired(),
                                   Email()])
    avatar = FileField('Avatar')
    submit = SubmitField('Save')
