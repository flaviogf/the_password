from flask import Blueprint, render_template

accounts = Blueprint('accounts', __name__)


@accounts.route('/')
@accounts.route('/accounts')
def pagination():
    return render_template('accounts_pagination.html', title='Accounts')
