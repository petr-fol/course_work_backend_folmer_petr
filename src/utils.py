from src.classes import Receipt
import json
import os


def get_operations():
    """
    Получает операции из JSON-файла.
    Returns:
        list: Список операций.
    """
    file_path = os.path.join('..', 'operations', 'operations.json')  # Путь к файлу операций
    with open(file_path, encoding='utf-8') as file:                  # Открываем файл
        operations_ = json.load(file)                                # Преобразуем JSON-файл в словарь

    return operations_


def is_correct_operation(operation):
    """
    Проверяет, является ли операция корректной.
    Args:
        operation (dict): Операция.

    Returns:
        bool: True, если операция корректна, иначе False.
    """
    counter = 0

    if "id" in operation and operation["id"]:
        counter += 1

    if "state" in operation and operation["state"]:
        counter += 1

    if "date" in operation and "T" in operation["date"]:
        counter += 1

    if ("operationAmount" in operation and "amount" in operation["operationAmount"] and
            operation["operationAmount"]["amount"]):
        counter += 1

    if ("operationAmount" in operation and "currency" in operation["operationAmount"] and
            "name" in operation["operationAmount"]["currency"] and operation["operationAmount"]["currency"]["name"]):
        counter += 1

    if ("operationAmount" in operation and "currency" in operation["operationAmount"] and
            "code" in operation["operationAmount"]["currency"] and operation["operationAmount"]["currency"]["code"]):
        counter += 1

    if "description" in operation and operation["description"]:
        counter += 1

    if "from" in operation and operation["from"]:
        counter += 1

    if "to" in operation and operation["to"]:
        counter += 1

    return counter == 9


def operations_as_objects(operations):
    """
    Преобразует операции в объекты класса Receipt.
    Args:
        operations (list): Список операций.

    Returns:
        list: Список объектов Receipt.
    """
    operations_objects = []
    for operation in operations:
        if is_correct_operation(operation):
            check_id = operation["id"]                                      # идентификатор операции
            check_state = operation["state"]                                # статус операции
            check_date = operation["date"]                                  # дата операции
            check_amount = operation["operationAmount"]["amount"]           # сумма операции
            check_name = operation["operationAmount"]["currency"]["name"]   # валюта операции
            check_code = operation["operationAmount"]["currency"]["code"]   # код валюты операции
            check_description = operation["description"]                    # описание операции
            check_from = operation["from"]                                  # отправитель карты
            check_to = operation["to"]                                      # получатель карты

            operations_objects.append(Receipt(check_id, check_state, check_date, check_amount, check_name,
                                              check_code, check_description, check_from, check_to))

    return operations_objects


def get_correct_date(date_time, date_or_time="date"):
    """
    Получает корректную дату или время из строки даты-времени.
    Args:
        date_time (str): Строка даты-времени.
        date_or_time (str): "date" для получения даты, "time" для получения времени.

    Returns:
        str or None: Корректная дата или время, либо None.
    """
    date_time_list = date_time.split('T')
    date_list = date_time_list[0].split('-')
    sort_date_list = [date_list[2], date_list[1], date_list[0]]
    if date_or_time == 'date':
        return '.'.join(sort_date_list)
    else:
        return None


def get_card_number(sender_or_recipient):
    """
    Получает номер карты из строки отправителя или получателя.
    Args:
        sender_or_recipient (str): Строка отправителя или получателя.

    Returns:
        str: Номер карты.
    """
    number_str = ""
    for symbol in sender_or_recipient:
        if symbol.isdigit():
            number_str += symbol
    return number_str


def get_card_description(sender, recipient=False):
    """
    Получает описание карты из строки отправителя или получателя.
    Args:
        sender (str): Строка отправителя.
        recipient (bool): Флаг, указывающий, является ли получатель.

    Returns:
        str: Описание карты.
    """
    global desc_card
    if recipient is False:
        desc_card = ""
        for symbol in sender:
            if not symbol.isdigit():
                desc_card += symbol
        return desc_card.strip()
    else:
        return "-> Счет"


def get_correct_card_number(card_number_str, sender_or_recipient_hide="sender"):
    """
    Получает корректный номер карты с заменой символов на "*", чтобы скрыть часть номера.
    Args:
        card_number_str (str): Строка с номером карты.
        sender_or_recipient_hide (str): "sender" для скрытия номера отправителя,
                                        "recipient" для скрытия номера получателя.

    Returns:
        str: Корректный номер карты.
    """
    global number_list_str
    number = get_card_number(card_number_str)
    if sender_or_recipient_hide == "sender":
        if len(number) == 16:
            number = number.replace(number[6:12], "******")
            number_list_str = [number[0:4], number[4:8], number[8:12], number[12:]]
        elif len(number) == 20:
            number = number.replace(number[6:16], "**********")
            number_list_str = [number[0:4], number[4:8], number[8:12], number[12:16], number[16:20]]
        return ' '.join(number_list_str)

    elif sender_or_recipient_hide == "recipient":
        number = number.replace(number[-6:-4], "**")
        number_list_str = [number[-6:-4], number[-4:]]
        return ''.join(number_list_str)
    else:
        return None


def print_receipt(receipt):
    """
    Выводит информацию о чеке.
    Args:
        receipt (Receipt): Объект чека.
    """
    amount = receipt.re_amount()
    date = get_correct_date(receipt.re_date())
    desc = receipt.re_description()
    currency = receipt.re_currency()
    currency_code = receipt.re_currency_code()

    card_number_sender = get_correct_card_number(get_card_number(receipt.sender))
    card_desc_sender = get_card_description(receipt.sender)

    card_number_recipient = get_correct_card_number(get_card_number(receipt.recipient), "recipient")
    card_desc_recipient = get_card_description(receipt.sender, True)

    return f"{date} {desc}\n" \
           f"{card_desc_sender} {card_number_sender} {card_desc_recipient} {card_number_recipient}\n" \
           f"{amount} {currency}\n"


def get_date_value(receipt_date):
    date_list = receipt_date.split(".")
    date_value = int(date_list[0]) + 365/12 * int(date_list[1]) + 365 * int(date_list[2])
    return date_value


def get_five_execute_operations(operations_objects_list):
    """
    Возвращает список пяти последних выполненных операций из заданного списка операций.

    Аргументы:
    - operations_objects_list (list): Список объектов операций.

    Возвращает:
    - five_execute_operations (list): Список пяти последних выполненных операций.

    """
    execute_operations = []
    five_execute_operations = []

    for operation in operations_objects_list:                    # Проверяем что операция корректная
        if operation.state == "EXECUTED":
            if get_date_value(get_correct_date(operation.date)):
                operation.date_value = get_date_value(get_correct_date(operation.date))
                execute_operations.append(operation)

    date_value_list = []
    for operation in execute_operations:
        date_value_list.append(operation.date_value)

    date_value_list.sort(reverse=True)
    five_execute_values = date_value_list[:5]
    for date_value in five_execute_values:
        for operation in execute_operations:
            if date_value == operation.date_value:
                five_execute_operations.append(operation)
                continue

    return five_execute_operations
