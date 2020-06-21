from flask import Flask, request
import config
from functools import wraps

from db import Data
from werkzeug.exceptions import BadRequest

app = Flask("API")
users = Data(config.data_path)


def response(fn):
    @wraps(fn)
    def resource(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except BadRequest as err:
            return {'error': str(err)}, 400
        except Exception as err:
            return {'error': str(err)}, 500
    return resource


@app.route("/user/<id>")
@response
def get_user_by_id(id):
    data = users.get_by_id(id)
    return data


@app.route("/user")
@response
def get_users():
    data = users.data
    return data


@app.route("/user", methods=["POST"])
@response
def add_user():
    data = request.get_json()
    result = users.add(data)
    users.sync()
    return result


@app.route("/user/<id>", methods=["PATCH"])
@response
def edit_user(id):
    data = request.get_json()
    result = users.update(id, data)
    users.sync()
    return result


@app.route("/user/<id>", methods=["DELETE"])
@response
def delete_user(id):
    result = users.delete(id)
    return result


app.run(host=config.host, port=config.port, debug=True)
