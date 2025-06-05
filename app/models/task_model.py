# app/models/task_model.py
from app.db import get_connection
import datetime

def get_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, description, is_completed, created_at, due_date, user_id FROM tasks")
    return cursor.fetchall()

def get_task_by_id(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, description, is_completed, created_at, due_date, user_id FROM tasks WHERE id = ?", task_id)
    return cursor.fetchone()

def insert_task(data):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tasks (description, is_completed, created_at, due_date, user_id)
        VALUES (?, ?, ?, ?, ?)
    """, data['description'], 0, datetime.datetime.now(), data['due_date'], data['user_id'])
    conn.commit()
    return True

def delete_task_by_id(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", task_id)
    conn.commit()
    return True
