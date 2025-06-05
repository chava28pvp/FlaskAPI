# app/routes/task_routes.py
from flask import Blueprint, request, jsonify
from app.models.task_model import get_all_tasks, get_task_by_id, insert_task, delete_task_by_id

task_bp = Blueprint('task_bp', __name__, url_prefix='/tasks')

@task_bp.route('', methods=['GET'])
def route_get_all_tasks():
    """
    Obtener todas las tareas
    ---
    responses:
      200:
        description: Lista de tareas
    """
    tasks = get_all_tasks()
    return jsonify([{
        'id': t[0], 'description': t[1], 'is_completed': bool(t[2]),
        'created_at': t[3], 'due_date': t[4], 'user_id': t[5]
    } for t in tasks])

@task_bp.route('/<int:task_id>', methods=['GET'])
def route_get_task(task_id):
    """
    Obtener tarea por ID
    ---
    parameters:
      - name: task_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Tarea encontrada
      404:
        description: Tarea no encontrada
    """
    t = get_task_by_id(task_id)
    if not t:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify({
        'id': t[0], 'description': t[1], 'is_completed': bool(t[2]),
        'created_at': t[3], 'due_date': t[4], 'user_id': t[5]
    })

@task_bp.route('', methods=['POST'])
def route_create_task():
    """
    Crear nueva tarea
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
            - description
            - due_date
            - user_id
          properties:
            description:
              type: string
            due_date:
              type: string
              format: date-time
            user_id:
              type: integer
    responses:
      201:
        description: Tarea creada
    """
    data = request.json
    insert_task(data)
    return jsonify({'message': 'Task created'}), 201

@task_bp.route('/<int:task_id>', methods=['DELETE'])
def route_delete_task(task_id):
    """
    Eliminar tarea por ID
    ---
    parameters:
      - name: task_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Tarea eliminada
    """
    delete_task_by_id(task_id)
    return jsonify({'message': 'Task deleted'})
