import json
from pathlib import Path

from settings import OPERATION_PATH
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
            amount=operation["operationAmount"]["amount"],
            currency_name=operation["operationAmount"]["currency"]["name"],
            description=operation["description"],
            from_account=operation.get("from", ""),
            to_account=operation["to"]
        )
        for operation in operations
        if operation
    ]


def executed_operations(operations):
    """
    Возвращает список выполненых операций
    :param operations:
    :return:
    """
    return [
        operation
        for operation in operations
        if operation.state == "EXECUTED"
    ]


def sort_operations_by_date(operations):
    """
    Сортирует список операций по дате
    :param operations:
    :return:
    """
    return sorted(operations, reverse=True)
