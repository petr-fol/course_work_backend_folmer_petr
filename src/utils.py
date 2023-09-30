def get_operations():
    import json
    with open('../operations/operations.json', encoding='utf-8') as file:
        operations_ = json.load(file)

        # for operation in operations_:
        #     new_operation = {
        #         "id_": operation["id"],
        #     }

    return operations_


def operations_as_objects(operations):

    from classes import Receipt
    operations_objects = []
    for operation in operations:
        operations_objects.append(Receipt(operation["id"],
                                          operation["state"],
                                          operation["date"],
                                          operation["operationAmount"]["amount"],
                                          operation["operationAmount"]["currency"]["name"],
                                          operation["operationAmount"]["currency"]["code"],
                                          operation["description"],
                                          operation["from"],
                                          operation["to"],
                                          ))

    return operations_objects


def get_correct_date(date_time, date_or_time="date"):
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
    alphabet = "".join([chr(i) for i in range(97, 123)]) + """!@#$%^&*()-_=+[{]}\|;:'/",<.>/?"""

    number_str = (sender_or_recipient.replace(alphabet, "").strip())
    return number_str


def get_card_description(sender, recipient=False):

    if recipient is False:
        for symbol in sender:
            desc_card = ""
            if not symbol.isdigit():
                desc_card += symbol
        return desc_card
    else:
        return "-> Счет"


def get_correct_card_number(card_number_str, sender_or_recipient_hide="sender"):
    number = get_card_number(card_number_str)
    if sender_or_recipient_hide == "sender":
        number.replace(number[6:12], "******")
        number_list_str = [number[0:4], number[4:8], number[8:12], number[12:]]
        return ' '.join(number_list_str)

    elif sender_or_recipient_hide == "recipient":
        number.replace(number[10:12], "**")
        number_list_str = [number[10:12], number[12:]]
        return''.join(number_list_str)
    else:
        return None


def print_receipt(receipt):
    amount = receipt.re_amount()
    date = get_correct_date(receipt.re_date())
    desc = receipt.re_description()
    currency = receipt.re_currency()
    currency_code = receipt.re_currency_code()
    card_number_sender = get_correct_card_number(receipt.re_card_number())
    card_desc_sender = get_card_description(receipt.re_card_number())
    card_number_recipient = get_correct_card_number(receipt.re_card_number(), "recipient")
    card_desc_recipient = get_card_description(receipt.re_card_number(), True)
    print(f"{date} {desc}")
    print(f"{card_desc_sender} {card_number_sender} {card_desc_recipient} {card_number_recipient}")
    print(f"{amount} {currency}.")


def get_five_execute_operations(operations_objects_list):
    execute_operations = []
    while len(operations_objects_list) < 5:
        for operation in operations_objects_list:
            if operation.re_state() == "execute":
                execute_operations.append(operation)
    return execute_operations
