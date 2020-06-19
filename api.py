import json
import os
import uuid

from flask import Flask, request
import config


app = Flask("API")


class User():
    def __init__(self, path):
        self.file_path = path
        self.last_id = None

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump({}, f)
            self.data = {}
        else:
            with open(path, "r") as f:
                self.data = json.load(f)

    def get_users_by_ids(self, ids):
        ids = ids.split(",")
        return {id: self.data.get(id, None) for id in ids}

    def update(self, id, data):
        if id in self.data:
            self.data[id].update(data)
            return self.data[id]
        else:
            return {"result": f"there is no user id {id} in the database"}

    def add_user(self, data):
        id = str(uuid.uuid4())
        data["id"] = id
        self.data.update({id: data})
        return data

    def delete(self, id):
        if id in self.data:
            del(self.data[id])
            return {"result": f"user id {id} was deleted"}
        else:
            return {"result": f"there is no user id {id} in the database"}

    def sync(self):
        with open(self.file_path, "w") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)


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
