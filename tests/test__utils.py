from settings import TEST_OPERATION_PATH
from src.utils import load_operations_from_json


def test__load_operations_from_json():
    operations = load_operations_from_json(TEST_OPERATION_PATH)
    assert len(operations) == 16
    assert isinstance(operations, list)
    assert isinstance(operations[0], dict)

def test__load_operations_instances():
