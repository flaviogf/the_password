from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import current_user, login_required

from app import db
from app.accounts.forms import CreateAccountForm
from app.models import Accounts

accounts = Blueprint('accounts', __name__)


@accounts.route('/')
@accounts.route('/accounts')
@login_required
def pagination():
    return render_template('accounts_pagination.html', title='Accounts')


@accounts.route('/accounts/create', methods=['GET', 'POST'])
@login_required
def create():
    form = CreateAccountForm()

    if form.validate_on_submit():
        account = Accounts(name=form.name.data,
                           login=form.login.data,
                           password=form.password.data,
                           user_id=current_user.get_id())

        db.session.add(account)

        db.session.commit()

        flash('Account created successfully.')

        return redirect(url_for('accounts.pagination'))

    return render_template('accounst_create.html',
                           title='Create Accounts',
                           form=form)
