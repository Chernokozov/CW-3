from settings import OPERATION_PATH, COUNT_OPERATIONS
from src.utils import (load_operations_from_json,
                       load_operations_instances,
                       executed_operations,
                       sort_operations_by_date)


def main():
    """
    Основной код программы
    :return:
    """
    operations = load_operations_from_json(OPERATION_PATH)
    operations_instances = load_operations_instances(operations)
    executed_operation = executed_operations(operations_instances)
    sorted_operations = sort_operations_by_date(executed_operation)[:COUNT_OPERATIONS]
    for operation in sorted_operations:
        print(operation)


if __name__ == '__main__':
    main()