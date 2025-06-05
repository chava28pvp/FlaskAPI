# app/routes/user_routes.py
from flask import Blueprint, request, jsonify
from app.models.user_model import get_all_users, get_user_by_id, insert_user, delete_user_by_id

user_bp = Blueprint('user_bp', __name__, url_prefix='/users')

@user_bp.route('', methods=['GET'])
def route_get_all_users():
    users = get_all_users()
    return jsonify([{
        'id': u[0], 'username': u[1], 'email': u[2], 'created_at': u[3], 'is_active': bool(u[4])
    } for u in users])

@user_bp.route('/<int:user_id>', methods=['GET'])
def route_get_user(user_id):
    u = get_user_by_id(user_id)
    if not u:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'id': u[0], 'username': u[1], 'email': u[2], 'created_at': u[3], 'is_active': bool(u[4])})

@user_bp.route('', methods=['POST'])
def route_create_user():
    data = request.json
    insert_user(data)
    return jsonify({'message': 'User created'}), 201

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def route_delete_user(user_id):
    delete_user_by_id(user_id)
    return jsonify({'message': 'User deleted'})
