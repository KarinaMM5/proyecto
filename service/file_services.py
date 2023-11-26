import json


def load_json(path_file):
    with open(path_file, "r") as file:
        return json.load(file)


def write_json(path_file, data):
    with open(path_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
