import json
import os
import uuid

from werkzeug.exceptions import BadRequest


class Data():
    def __init__(self, path):
        self.file_path = path

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump({}, f)
            self.data = {}
        else:
            with open(path, "r") as f:
                self.data = json.load(f)

    def get_by_id(self, id):
        if id not in self.data:
            raise BadRequest(f"there is no user id {id} in the database")
        return self.data.get(id)

    def update(self, id, data):
        if id not in self.data:
            raise BadRequest(f"there is no user id {id} in the database")
        self.data[id].update(data)
        return self.data[id]

    def add(self, data):
        if "name" not in data:
            raise BadRequest(f"there is no field 'name' in the data")
        id = str(uuid.uuid4())
        data["id"] = id
        self.data.update({id: data})
        return data

    def delete(self, id):
        if id not in self.data:
            raise BadRequest(f"there is no user id {id} in the database")
        del(self.data[id])
        return {"result": f"user id {id} was deleted"}

    def sync(self):
        with open(self.file_path, "w") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)
