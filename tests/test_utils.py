from src.utils import *


def test_get_operations():
    operations = get_operations()

    # Проверяем, что функция возвращает список
    assert isinstance(operations, list)


def check_correct_operation(operation):
    """
    Проверяет, является ли операция корректной.
    Args:
        operation (dict): Операция.

    Returns:
        dict or None: Операция, если она корректна, иначе None.
    """
    if operation:
        return operation
    else:
        return None


def test_is_correct_operation():
    # Проверяем корректную операцию
    operation = {
        "id": 1,
        "state": "completed",
        "date": "2021-09-30",
        "operationAmount": {
            "amount": 100,
            "currency": {
                "name": "USD",
                "code": "usd"
            }
        },
        "description": "Операция 1",
        "from": "Account A",
        "to": "Account B"
    }
    result = is_correct_operation(operation)
    assert result == True


def test_operations_as_objects():
    # Проверяем список корректных операций
    operations = [
        {
            "id": 1,
            "state": "completed",
            "date": "2021-09-30",
            "operationAmount": {
                "amount": 100,
                "currency": {
                    "name": "USD",
                    "code": "usd"
                }
            },
            "description": "Операция 1",
            "from": "Account A",
            "to": "Account B"
        },
        {
            "id": 2,
            "state": "completed",
            "date": "2021-10-01",
            "operationAmount": {
                "amount": 200,
                "currency": {
                    "name": "EUR",
                    "code": "eur"
                }
            },
            "description": "Операция 2",
            "from": "Account B",
            "to": "Account C"
        }
    ]
    result = operations_as_objects(operations)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(receipt, Receipt) for receipt in result)


def test_get_correct_date():
    # Проверяем корректную дату
    date = "2019-08-26T10:50:58.294041"
    result = get_correct_date(date)
    assert result == "26.08.2019"


def test_get_card_number():
    # Проверяем корректный номер карты
    card_number_str = "Maestro 1596837868705199"
    result = get_card_number(card_number_str)
    assert result == "1596837868705199"
    card_number_str_20 = "Maestro 15968378687051991111"
    result = get_card_number(card_number_str_20)
    assert result == "15968378687051991111"


def test_get_card_description():
    result = get_card_description("Maestro 1596837868705199")
    assert result == "Maestro"


def test_get_correct_card_number():
    # Проверяем корректный номер карты
    result = get_correct_card_number("1111222233334444")
    assert result == "1111 22** **** 4444"
    result = get_correct_card_number("11112222333344445555")
    assert result == "1111 22** **** **** 5555"

    result = get_correct_card_number("1111222233334444", "recipient")
    assert result == "**4444"
    result = get_correct_card_number("11112222333344445555", "recipient")
    assert result == "**5555"
