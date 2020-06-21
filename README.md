### Usage

1) `pip install -r requirements.txt`
2) `python api.py`
3) Requests to api:

- `POST /user` - add new user to the database.
```
Data example:
    { 
        "name": "Name",
        "age": 21
    }

Response example:
    {
        "age": 21,
        "id": "a393e734-e59c-46db-b790-1f58e714cf14",
        "name": "Name"
    }
```

-  `GET /user/<id>` - get user by id.
```
Response example:
   {
        "age": 21,
        "id": "639cd882-0906-447f-b4f1-675c10d20bcd",
        "name": "New_name"
    }
```

- `GET /user` - get all users.
```
Response example:
    {
        "639cd882-0906-447f-b4f1-675c10d20bcd": {
            "age": 21,
            "id": "639cd882-0906-447f-b4f1-675c10d20bcd",
            "name": "New_name"
        },
        "d2c264a9-4e25-4033-b46d-7b2982cf1f81": {
            "age": 21,
            "id": "d2c264a9-4e25-4033-b46d-7b2982cf1f81",
            "name": "Name"
        }
    }
```
- `PATCH /user/<id>` - edit user data by id.
```
Data example:

    { 
        "age": 25
    }

Response example:
    {
        "age": 25,
        "id": "a393e734-e59c-46db-b790-1f58e714cf14",
        "name": "Name"
    }
```
If id is not in the database api returns:
```
    {
        "result": "there is no user id <id> in the database"
    }
```
- `DELETE /user/<id>` - delete user by id.
```
Response example:
    {
        "result": "user id a393e734-e59c-46db-b790-1f58e714cf14 was deleted"
    }
```
If id is not in the database api returns:
```
    {
        "result": "there is no user id <id> in the database"
    }
```
