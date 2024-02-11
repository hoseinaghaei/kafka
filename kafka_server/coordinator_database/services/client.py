import threading
from SADProject.coordinator_database import config
import json
import os.path

lock = threading.Lock()


def init_clients_file():
    path = f'./{config.CLIENT_DATABASE_FILE_PATH}'
    check_file = os.path.isfile(path)
    if not check_file:
        with open(path, 'w') as f:
            f.write(json.dumps({"clients": []}))


def add_client(data):
    with lock:
        init_clients_file()
        json_data = None
        with open(config.CLIENT_DATABASE_FILE_PATH, 'r') as f:
            json_data = json.load(f)
            f.close()
        with open(config.CLIENT_DATABASE_FILE_PATH, 'w') as f:
            json_data["clients"].append(data)
            f.write(json.dumps(json_data))
            f.close()


def get_all_clients():
    with lock:
        init_clients_file()
        with open(config.CLIENT_DATABASE_FILE_PATH, 'r') as f:
            json_data = json.load(f)

    return json_data["clients"]