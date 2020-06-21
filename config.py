import os

host = os.environ.get("api_host", "0.0.0.0")
port = os.environ.get("api_port", "8080")
data_path = os.environ.get("data_path", "./User.json")
