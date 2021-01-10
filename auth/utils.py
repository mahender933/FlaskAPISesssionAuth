from functools import wraps

from flask import session


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'user_id' in session:
            return f(*args, **kwargs)
        else:
            return {'msg': "Session Expired. Please login Again using /login endpoint"}, 440
    return wrap



