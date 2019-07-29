from flask import Blueprint, render_template
from flask_login import login_required

accounts = Blueprint('accounts', __name__)


@accounts.route('/')
@accounts.route('/accounts')
@login_required
def pagination():
    return render_template('accounts_pagination.html', title='Accounts')
