from flask import Blueprint

from ..models import User

user_routes = Blueprint('users', __name__)

@user_routes.route('/<int:id>')
def user_by_id(id):
    user = User.query.get(id)
    pass


@user_routes.route('/all')
def all_users():
    users = User.query.all()
    pass