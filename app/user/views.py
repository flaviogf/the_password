import secrets
from os import path

from flask import (Blueprint, current_app, flash, redirect, render_template,
                   request, url_for)
from flask_login import current_user, login_required, login_user, logout_user
from PIL import Image

from app import db
from app.models import User
from app.user.forms import LoginForm, ProfileForm

user = Blueprint('user', __name__)


@user.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('accounts.pagination'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.authenticate(form.password.data):
            login_user(user, remember=form.remember.data)

            next_url = request.args.get('next')

            return redirect(next_url or url_for('accounts.pagination'))

        flash('Email or password incorrect.', 'danger')

    return render_template('user_login.html',
                           title='Login',
                           form=form)


@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user.login'))


@user.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()

    if form.validate_on_submit():
        if form.avatar.data:
            current_user.avatar = save_avatar(form.avatar.data)

        current_user.name = form.name.data
        current_user.email = form.email.data

        db.session.commit()

        return redirect(url_for('accounts.pagination'))

    elif request.method == 'GET':
        form.name.data = current_user.name
        form.email.data = current_user.email

    avatar = url_for('static',
                     filename=f'uploads/{current_user.avatar}')

    return render_template('user_profile.html',
                           title='Profile',
                           form=form,
                           avatar=avatar)


def save_avatar(file):
    image = Image.open(file)

    image.thumbnail((100, 100))

    upload_folder = current_app.config.get('UPLOAD_FOLDER')

    avatar = f'{secrets.token_hex()}.png'

    filename = path.join(upload_folder, avatar)

    image.save(filename)

    return avatar
