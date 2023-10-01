from classes import Receipt
import json


def get_operations():
    """
    Получает операции из JSON-файла.
    Returns:
        list: Список операций.
    """
    with open('../operations/operations.json', encoding='utf-8') as file:
        operations_ = json.load(file)

    return operations_


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


def is_correct_operation(operation):
    """
    Проверяет, является ли операция корректной.
    Args:
        operation (dict): Операция.

    Returns:
        bool: True, если операция корректна, иначе False.
    """
    try:
        check_correct_operation(operation["id"])
        check_correct_operation(operation["state"])
        check_correct_operation(operation["date"])
        check_correct_operation(operation["operationAmount"]["amount"])
        check_correct_operation(operation["operationAmount"]["currency"]["name"])
        check_correct_operation(operation["operationAmount"]["currency"]["code"])
        check_correct_operation(operation["description"])
        check_correct_operation(operation["from"])
        check_correct_operation(operation["to"])
        return True
    except:
        return False


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
            check_id = check_correct_operation(operation["id"])
            check_state = check_correct_operation(operation["state"])
            check_date = check_correct_operation(operation["date"])
            check_amount = check_correct_operation(operation["operationAmount"]["amount"])
            check_name = check_correct_operation(operation["operationAmount"]["currency"]["name"])
            check_code = check_correct_operation(operation["operationAmount"]["currency"]["code"])
            check_description = check_correct_operation(operation["description"])
            check_from = check_correct_operation(operation["from"])
            check_to = check_correct_operation(operation["to"])
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
    time_list = date_time_list[1].split(':')
    sort_date_list = [date_list[2], date_list[1], date_list[0]]
    if date_or_time == 'date':
        return '.'.join(sort_date_list)
    elif date_or_time == 'time':
        return time_list
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
    if recipient is False:
        desc_card = ""
        for symbol in sender:
            if not symbol.isdigit():
                desc_card += symbol
        return desc_card
    else:
        return "-> Счет"


def get_correct_card_number(card_number_str, sender_or_recipient_hide="sender"):
    """
    Получает корректный номер карты с заменойсимволов на "*", чтобы скрыть часть номера.
    Args:
        card_number_str (str): Строка с номером карты.
        sender_or_recipient_hide (str): "sender" для скрытия номера отправителя,
                                        "recipient" для скрытия номера получателя.

    Returns:
        str: Корректный номер карты.
    """
    number = get_card_number(card_number_str)
    if sender_or_recipient_hide == "sender":
        number_list_str = []
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
    card_desc_sender = get_card_description(get_card_number(receipt.sender))

    card_number_recipient = get_correct_card_number(get_card_number(receipt.recipient), "recipient")
    card_desc_recipient = get_card_description(get_card_number(receipt.sender), True)

    print(f"{date} {desc}")
    print(f"{card_desc_sender} {card_number_sender} {card_desc_recipient} {card_number_recipient}")
    print(f"{amount} {currency}\n")


def get_five_execute_operations(operations_objects_list):
    """
    Получает пять выполненных операций из списка операций-объектов.
    Args:
        operations_objects_list (list): Список операций-объектов.

    Returns:
        list: Список пяти выполненных операций.
    """
    execute_operations = []
    for operation in operations_objects_list:
        if operation.state == "EXECUTED":
            execute_operations.append(operation)
    return execute_operations[0:5]

