def get_operations():
    import json
    with open('../operations/operations.json', 'r') as file:
        operations_ = json.load(file)
    return operations_


def operations_as_objects(operations):

    from classes import Receipt
    operations_objects = []
    for operation in operations:
        operations_objects.append(Receipt(operation["id"],
                                          operation["state"],
                                          operation["date"],
                                          operation["amount"],
                                          operation["currency"],
                                          operation["currency_code"],
                                          operation["description"],
                                          operation["sender"],
                                          operation["recipient"]
                                          ))

    return operations_objects


def get_correct_date(date_time, date_or_time="date"):
    date_time_list = date_time.split('T')
    date_list = date_time_list[0].split('-')
    time_list = date_time_list[1].split(':')
    if date_or_time == 'date':
        return date_list
    elif date_or_time == 'time':
        return time_list
    else:
        return None

def print_receipt(receipt_object):
