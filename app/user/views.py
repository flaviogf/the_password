from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_user, logout_user

from app.models import User
from app.user.forms import LoginForm

user = Blueprint('user', __name__)


@user.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.authenticate(form.password.data):
            login_user(user, remember=form.remember.data)

            next_url = request.args.get('next')

            return redirect(next_url or url_for('accounts.pagination'))

        flash('Email or password incorrect.')

    return render_template('login.html',
                           title='Login',
                           form=form)


@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user.login'))
