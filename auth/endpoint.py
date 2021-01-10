from flask import Blueprint, request, session
from marshmallow import ValidationError
from sqlalchemy import exc

from .models import User
from .schema import user_login_schema, user_sign_up_schema
from .utils import login_required

auth_blueprint = Blueprint('auth_api', __name__)


@auth_blueprint.route("/api", methods=["GET"])
def api_info():
    return {
        "/sign-up": "Sign Up or Create a new user",
        "/login": "Login as a user",
        "/logout": "Logout",
        "/profile": "Get profile related information",
    }


@auth_blueprint.route("/sign-up", methods=["POST"])
def sign_up():
    json_data = request.get_json()
    if not json_data:
        return {"message": "No input data provided"}, 400
    # Validate and deserialize input
    try:
        data = user_sign_up_schema.load(json_data)
        user = User.query.filter_by(username=data.get('username')).first()
        if user:
            # User with same username already exists
            return {'msg': "User already exists with the given username"}, 409
        user_obj = User(
            username=data.get('username'),
            email=data.get('email'),
            phone_number=data.get('phone_number')
        )
        user_obj.set_password(data.get('password'))
        user_obj.save()
        session['user_id'] = user_obj.id

    except ValidationError as err:
        return err.messages, 422
    except exc.IntegrityError:
        return {"msg": "Unique constraint failed for email"}, 409
    return {'msg': "Successfully signed up !"}, 201


@auth_blueprint.route("/login", methods=["POST"])
def login():
    json_data = request.get_json()
    if not json_data:
        return {"message": "No input data provided"}, 400
    try:
        data = user_login_schema.load(json_data)
        user = User.query.filter_by(username=data.get('username'), ).first()
        if not user:
            return {"msg": "No user found with given credentials"}
        verified = user.check_password(password=data.get('password'))
        if not verified:
            return {"msg": "Invalid Password"}, 401
        session['user_id'] = user.id
        return {'msg': "Successfully Logged In"}, 200

    except ValidationError as err:
        return err.messages, 401


@auth_blueprint.route("/logout", methods=["GET"])
def logout():
    session.pop('user_id', None)
    return {"msg": "Successfully Logged out"}, 200


@auth_blueprint.route("/profile/", methods=["GET"])
@login_required
def profile():
    user_id = session.get('user_id')
    user_obj = User.query.get(user_id)
    return {"username": user_obj.username,
            "email": user_obj.email,
            "phone_number": user_obj.phone_number,
            "password_hash": user_obj.password_hash,
            "msg": "Success"}, 200
