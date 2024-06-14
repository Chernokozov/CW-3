import json
from pathlib import Path


def load_operations_from_json(path):
    """
    Загружает операции из файла json
    :param path:
    :return:
    """
    with open(path, encoding="utf-8") as file:
        return json.load(file)
