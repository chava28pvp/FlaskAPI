# app/models/user_model.py
from app.db import get_connection
import datetime

def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email, created_at, is_active FROM users")
    return cursor.fetchall()

def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email, created_at, is_active FROM users WHERE id = ?", user_id)
    return cursor.fetchone()

def insert_user(data):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO users (username, password, email, created_at, is_active)
        VALUES (?, ?, ?, ?, ?)
    """, data['username'], data['password'], data['email'], datetime.datetime.now(), 1)
    conn.commit()
    return True

def delete_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", user_id)
    conn.commit()
    return True
