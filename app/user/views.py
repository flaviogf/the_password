from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, logout_user

from app.decorators import redirect_authenticated_user
from app.models import User
from app.user.forms import LoginForm, ProfileForm

user = Blueprint('user', __name__)


@user.route('/login', methods=['GET', 'POST'])
@redirect_authenticated_user
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.find_by(email=form.email.data)

        if not user or not user.login(form.password.data, form.remember.data):
            flash('Email or password incorrect.', 'danger')
            return render_template('user_login.html', title='Login', form=form)

        return redirect(request.args.get('next') or url_for('accounts.pagination'))

    return render_template('user_login.html', title='Login', form=form)


@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user.login'))


@user.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()

    if form.validate_on_submit():
        current_user.update(name=form.name.data,
                            email=form.email.data,
                            avatar=form.avatar.data)

        current_user.save()

        return redirect(url_for('accounts.pagination'))

    elif request.method == 'GET':
        form.name.data = current_user.name
        form.email.data = current_user.email

    return render_template('user_profile.html',
                           title='Profile',
                           form=form)
