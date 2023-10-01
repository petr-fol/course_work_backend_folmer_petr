from src import utils
from src.classes import Receipt
from src.utils import print_receipt


def test_get_operations():
    operations = utils.get_operations()
    assert len(operations) > 0
    assert len(operations[0]) > 0
    assert type(operations) == list
    assert type(operations[0]) == dict
    assert type(operations[0]['name']) == str


def test_check_correct_operation():
    operations = utils.get_operations()
    operation = utils.operations_as_objects(operations)
    operation = utils.check_correct_operation(operation[0])
    assert type(operation) == dict
    assert type(operation['name']) == str
    assert type(operation['description']) == str
    assert type(operation['parameters']) == list
    assert len(operation['parameters']) > 0
    assert type(operation['parameters'][0]) == dict
    assert type(operation['parameters'][0]['name']) == str
    assert type(operation['parameters'][0]['description']) == str
    assert type(operation['parameters'][0]['type']) == str
    assert type(operation['parameters'][0]['required']) == bool
    assert type(operation['parameters'][0]['in']) == str
    assert type(operation['parameters'][0]['schema']) == dict
    assert type(operation['parameters'][0]['schema']['type']) == str
    assert type(operation['parameters'][0]['schema']['properties']) == dict


def test_is_correct_operation():
    operations = utils.get_operations()
    operation = utils.operations_as_objects(operations)
    operation = utils.check_correct_operation(operation[0])
    assert utils.is_correct_operation(operation) is True


def test_operations_as_objects():
    operations = utils.get_operations()
    operation = utils.operations_as_objects(operations)
    operation = utils.check_correct_operation(operation[0])
    assert utils.operations_as_objects(operations) == [operation]


def test_get_correct_date():
    date = utils.get_correct_date("2019-07-03T18:35:29.512364", "date")
    assert type(date) == str
    assert len(date) > 0
    assert utils.get_correct_date("2019-07-03T18:35:29.512364", "date") == "03.07.2019"
    time = utils.get_correct_date("2019-07-03T18:35:29.512364", "time")
    assert type(time) == list
    assert len(time) > 0
    assert utils.get_correct_date("2019-07-03T18:35:29.512364", "time") == ["18", "35", "29.512364"]


def test_get_card_number():
    number = utils.get_card_number("Maestro 1596837868705199")
    assert type(number) == str
    assert len(number) > 0
    assert int(number) == 1596837868705199


def test_get_card_description():
    description = utils.get_card_description("Maestro 1596837868705199")
    assert type(description) == str
    assert len(description) > 0
    assert description == "Maestro"


def test_get_correct_card_number():
    number = utils.get_correct_card_number("1596837868705199")
    assert type(number) == str
    assert len(number) > 0
    assert number == "1596 83** **** 5199"
    number = utils.get_correct_card_number("1596837868705199, 'recipient'")
    assert type(number) == str
    assert len(number) > 0
    assert number == "**5199"


def test_print_receipt():
    receipt = Receipt(441945886, "EXECUTED", "2019-08-26T10:50:58.294041",
                      "31957.58", "руб.", "RUB")
    assert type(receipt) == Receipt
    assert print_receipt(receipt) == "26.08.2019 Перевод организации\n" \
                                     "1596 83** **** 5199 -> Счет **9589\n" \
                                     "31957.58 руб."


def test_get_five_execute_operations():
    operations = utils.get_operations()
    assert len(utils.get_five_execute_operations(operations)) == 5
