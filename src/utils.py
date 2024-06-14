import json
from pathlib import Path

from src.operations import Operation


def load_operations_from_json(path):
    """
    Загружает операции из файла json
    :param path:
    :return:
    """
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def load_operations_instances(operations):
    """
    Создает экземпляры класса Operation из списка операций
    :param operations:
    :return:
    """
    return [
        Operation(
            date=operation["date"],
            state=operation["state"],
            amount=operation["amount"],
            currency_name=operation["currency_name"],
            description=operation["description"],
            from_account=operation["from"],
            to_account=operation["to"]
        )
        for operation in operations
        if operation
    ]
