import functools

from flask import redirect
from flask_login import current_user


def redirect_authenticated_user(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect('/')
        return fn(*args, **kwargs)
    return wrapper
