import functools
from typing import Callable
from flask import redirect, url_for, session, flash

def required_login(f: Callable) -> Callable:
    @functools.wraps(f)
    def decorator_function(*args, **kwargs):
        if not session.get('username'):
            flash('Please log in first', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorator_function

