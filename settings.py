from pathlib import Path

ROOT_PATH = Path(__file__).parent
OPERATION_PATH = ROOT_PATH.joinpath("src", "data", "operations.json")
TEST_OPERATION_PATH = ROOT_PATH.joinpath("tests", "test__operations.json")
COUNT_OPERATIONS = 5
