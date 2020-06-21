from flask import Flask, request
import config

from db import Data

app = Flask("API")
users = Data(config.data_path)


@app.route("/user/<id>")
def get_user_by_id(id):
    data = users.get_by_id(id)
    return data


@app.route("/user")
def get_users():
    data = users.data
    return data


@app.route("/user", methods=["POST"])
def add_user():
    data = request.get_json()
    result = users.add(data)
    users.sync()
    return result


@app.route("/user/<id>", methods=["PATCH"])
def edit_user(id):
    data = request.get_json()
    result = users.update(id, data)
    users.sync()
    return result


@app.route("/user/<id>", methods=["DELETE"])
def delete_user(id):
    result = users.delete(id)
    return result


app.run(host=config.host, port=config.port, debug=True)
