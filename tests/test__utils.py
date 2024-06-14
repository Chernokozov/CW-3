from settings import TEST_OPERATION_PATH
from src.operations import Operation
from src.utils import load_operations_from_json, load_operations_instances


def test__load_operations_from_json():
    operations = load_operations_from_json(TEST_OPERATION_PATH)
    assert len(operations) == 16
    assert isinstance(operations, list)
    assert isinstance(operations[0], dict)


def test__load_operations_instances(operations_json):
    operations = load_operations_instances(operations_json)
    assert len(operations) == 15
    assert isinstance(operations, list)
    assert isinstance(operations[0], Operation)
    assert operations[0].date == "2019-08-26T10:50:58.294041"
    assert operations[0].from_account == ""
