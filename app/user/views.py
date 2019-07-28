from flask import Blueprint, render_template, request, redirect, url_for


user = Blueprint('user', __name__)


@user.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('accounts.pagination'))

    return render_template('login.html', title='Login')
