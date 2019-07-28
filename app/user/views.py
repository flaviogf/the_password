from flask import Blueprint, redirect, render_template, request, url_for

user = Blueprint('user', __name__)


@user.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('accounts.pagination'))

    return render_template('login.html', title='Login')
