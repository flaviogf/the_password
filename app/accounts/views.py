from flask import (Blueprint, abort, flash, redirect, render_template, request,
                   url_for)
from flask_login import current_user, login_required

from app.accounts.forms import CreateAccountForm
from app.models import Accounts

accounts = Blueprint('accounts', __name__)


@accounts.route('/')
@accounts.route('/accounts')
@login_required
def pagination():
    page = request.args.get('page', 1, type=int)

    accounts = Accounts.paginate(page)

    return render_template('accounts_pagination.html',
                           title='Search Accounts',
                           accounts=accounts)


@accounts.route('/accounts/create', methods=['GET', 'POST'])
@login_required
def create():
    form = CreateAccountForm()

    if form.validate_on_submit():
        account = Accounts(name=form.name.data,
                           login=form.login.data,
                           password=form.password.data,
                           user_id=current_user.get_id())

        account.save()

        flash('Account created successfully.', 'success')

        return redirect(url_for('accounts.pagination'))

    return render_template('accounts_create.html',
                           title='Create Account',
                           form=form)


@accounts.route('/accounts/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    account = Accounts.find_by(id=id, user_id=current_user.get_id())

    if not account:
        abort(404)

    form = CreateAccountForm()

    if form.validate_on_submit():
        account.update(name=form.name.data,
                       login=form.login.data,
                       password=form.password.data)

        account.save()

        flash('Account updated successfully.', 'success')

        return redirect(url_for('accounts.pagination'))

    elif request.method == 'GET':
        form.name.data = account.name
        form.login.data = account.login
        form.password.data = account.password

    return render_template('accounts_create.html',
                           title='Update Account',
                           form=form)
