import json
import os
import uuid

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
        return self.data.get(id, None)

    def update(self, id, data):
        if id in self.data:
            self.data[id].update(data)
            return self.data[id]
        else:
            return {"result": f"there is no user id {id} in the database"}

    def add(self, data):
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
