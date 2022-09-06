from flask import Flask, jsonify, request
from models import User, Task
from deta import Deta, Base
import db


app = Flask(__name__)


@app.route('/home')
def home():
    return jsonify({'message': 'Welcome to the task distributor API'})


@app.route('/new_user', methods=['POST'])
def create_user():
    first_name = request.json.get('first_name').capitalize()
    last_name = request.json.get('last_name').capitalize()
    email = request.json.get('email')
    password = request.json.get('password')

    new_user = User(first_name=first_name, last_name=last_name, email=email, password=password)
    new_user = db.db_users.put({
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email,
                    "password": password}, key=email)
    return jsonify(message='User created successfully.'), 201


@app.route('/new_task', methods=['POST'])
def create_task():
    num= request.json.get('num')
    title = request.json.get('title').capitalize()
    desc = request.json.get('desc')
    task = db.db_tasks.get(num)
    if not task:
        new_task = Task(num =num, title=title, desc=desc)
        new_task = db.db_tasks.put({
                        "num": num,
                        "title": title,
                        "desc": desc}, key=num)
        return jsonify(message='Task created successfully.'), 201
    else:
        return jsonify(message='Task already exists.'), 409


@app.route('/tasks', methods=['GET'])
def get_tasks():
    res = db.db_tasks.fetch()
    all_tasks = res.items
    return jsonify(all_tasks)


@app.route('/users', methods=['GET'])
def get_users():
    res = db.db_users.fetch()
    all_tasks = res.items
    return jsonify(all_users)


@app.route('/update_task', methods=['PUT'])
def update_task():
    task_key = request.json.get('num')
    task = db.db_tasks.get(task_key)
    if task:
        title = request.json.get('new_title').capitalize()
        desc = request.json.get('new_desc')
        updates = {
            "title": title,
            "desc": desc
        }
        db.db_tasks.update(updates, task_key)
        return jsonify(message='Task updated successfully.'), 202
    else:
        return jsonify(message='Task not found.'), 404


@app.route('/remove_task/<int:num>', methods=['DELETE'])
def remove_task(num: int):
    task = db.db_tasks.get(str(num))
    if task:
        db.db_tasks.delete(str(num))
        return jsonify(message='Task deleted successfully.'), 202
    else:
        return jsonify(message='That task does not exist'), 404


if __name__ == "__main__":
    app.run(debug=True)