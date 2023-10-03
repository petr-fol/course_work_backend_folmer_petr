from src.utils import is_correct_operation


def test_is_correct_operation():
    """
    Тестирует функцию is_correct_operation().
    """

    # Проверяем некорректную операцию
    operation = {
        "id": 1,
        "state": "EXECUTED",
        "date": "2021.09.30",
        "operationAmount": {
            "amount": "100",
            "currency": {
                "name": "USD",
                "code": "usd"
            }
        },
        "description": "Операция 1",
        "from": "Account A 11112222333344445555",
        "to": "Account 1111222233334444"
    }
    result = is_correct_operation(operation)
    assert result is False

    operation = {
        "id": 1,
        "state": "EXECUTED",
        # Отсутствует поле "date"
        "operationAmount": {
            "amount": 100,
            "currency": {
                "name": "USD",
                "code": "usd"
            }
        },
        "description": "Операция 1",
        "from": "Account A 11112222333344445555",
        "to": "Account 1111222233334444"
    }
    result = is_correct_operation(operation)
    assert result is False

    operation = {
        "id": 1,
        "state": "EXECUTED",
        # Некорректный формат
        "date": "2021-09-30",
        "operationAmount": {
            "amount": 100,
            "currency": {
                "name": "USD",
                "code": "usd"
            }
        },
        "description": "Операция 1",
        "from": "Account A 11112222333344445555",
        "to": "Account 1111222233334444"
    }
    result = is_correct_operation(operation)
    assert result is False

    # Проверяем корректную операцию
    operation = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }
    result = is_correct_operation(operation)
    assert result is True

    # Добавляем дополнительные тесты для покрытия более 80%
    operation = {
        "id": 1,
        "state": "EXECUTED",
        "date": "2021.09.30",
        "operationAmount": {
            "amount": "100",
            "currency": {
                "name": "USD",
                "code": "usd"
            }
        },
        "description": "Операция 1",
        "from": "Account A 11112222333344445555",
        "to": "Account 1111222233334444"
    }
    result = is_correct_operation(operation)
    assert result is False

    operation = {
        "id": 1,
        "state": "EXECUTED",
        "date": "2021.09.30",
        "operationAmount": {
            "amount": "100",
            "currency": {
                "name": "USD",
                "code": "usd"
            }
        },
        # Отсутствует поле "description"
        "from": "Account A 11112222333344445555",
        "to": "Account 1111222233334444"
    }
    result = is_correct_operation(operation)
    assert result is False

    operation = {
        "id": 1,
        "state": "EXECUTED",
        "date": "2021.09.30",
        "operationAmount": {
            "amount": "100",
            "currency": {
                "name": "USD",
                "code": "usd"
            }
        },
        "description": "Операция 1",
        # Отсутствует поле "from"
        "to": "Account 1111222233334444"
    }
    result = is_correct_operation(operation)
    assert result is False


operation = {
        "id": 1,
        "state": "EXECUTED",
        "date": "2021.09.30",
        "operationAmount": {
            "amount": "100",
            "currency": {
                "name": "USD",
                "code": "usd"
            }
        },
        "description": "Операция 1",
        "from": "Account A 11112222333344445555",
        # Отсутствует поле "to"
    }
result = is_correct_operation(operation)
assert result is False
