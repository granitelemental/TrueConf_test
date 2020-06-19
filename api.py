from flask import Flask, request
import config

from db import User


app = Flask("API")

users = User(config.data_path)


@app.route("/user/<ids>")
def get_users_by_ids(ids):
    data = users.get_users_by_ids(ids)
    return data


@app.route("/user")
def get_users():
    data = users.data
    return data


@app.route("/user", methods=["POST"])
def add_user():
    data = request.get_json()
    result = users.add_user(data)
    users.sync()
    return result


@app.route("/user/<id>", methods=["PATCH"])
def edit_user(id):
    data = request.get_json()
    result = users.update(id, data)
    users.sync()
    return result


@app.route("/user/<id>", methods=["PUT"])
def change_user(id):
    data = request.get_json()
    result = users.update(id, data)
    users.sync()
    return result


@app.route("/user/<id>", methods=["DELETE"])
def delete_user(id):
    result = users.delete(id)
    return result


app.run(host=config.host, port=config.port , debug=True)
