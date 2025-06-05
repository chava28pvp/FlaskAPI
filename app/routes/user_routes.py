# app/routes/user_routes.py
from flask import Blueprint, request, jsonify
from app.models.user_model import get_all_users, get_user_by_id, insert_user, delete_user_by_id

user_bp = Blueprint('user_bp', __name__, url_prefix='/users')

@user_bp.route('', methods=['GET'])
def route_get_all_users():
    """
    Obtener todos los usuarios
    ---
    responses:
      200:
        description: Lista de usuarios
    """
    users = get_all_users()
    return jsonify([{
        'id': u[0], 'username': u[1], 'email': u[2], 'created_at': u[3], 'is_active': bool(u[4])
    } for u in users])

@user_bp.route('/<int:user_id>', methods=['GET'])
def route_get_user(user_id):
    """
    Obtener usuario por ID
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Usuario encontrado
      404:
        description: Usuario no encontrado
    """
    u = get_user_by_id(user_id)
    if not u:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'id': u[0], 'username': u[1], 'email': u[2], 'created_at': u[3], 'is_active': bool(u[4])})

@user_bp.route('', methods=['POST'])
def route_create_user():
    """
    Crear nuevo usuario
    ---
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - username
            - password
            - email
          properties:
            username:
              type: string
            password:
              type: string
            email:
              type: string
    responses:
      201:
        description: Usuario creado
    """
    data = request.json
    insert_user(data)
    return jsonify({'message': 'User created'}), 201

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def route_delete_user(user_id):
    """
    Eliminar usuario por ID
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Usuario eliminado
    """
    delete_user_by_id(user_id)
    return jsonify({'message': 'User deleted'})
