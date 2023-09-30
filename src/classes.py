class Receipt:
    def __init__(self, id_, state, date, amount, name, code, description, from_, to):
        self.id = id_
        self.state = state
        self.date = date
        self.amount = amount
        self.currency = name
        self.currency_code = code
        self.description = description
        self.sender = from_
        self.recipient = to

    def __str__(self):
        return (f'Receipt {self.id} from {self.sender}'
                f' to {self.recipient}'
                f' with amount {self.amount} {self.currency}')

    def __repr__(self):
        return (f'Receipt {self.id} from {self.sender}'
                f' to {self.recipient}'
                f' with amount {self.amount} {self.currency}')

    def re_id(self):
        return self.id

    def re_state(self):
        return self.state

    def re_date(self):
        return self.date

    def re_amount(self):
        return self.amount

    def re_currency(self):
        return self.currency

    def re_currency_code(self):
        return self.currency_code

    def re_description(self):
        return self.description

    def re_sender(self):
        return self.sender

    def re_recipient(self):
        return self.recipient


class Bank_card_number:
    def __init__(self, description, number):
        self.description = description
        self.number = number

    def re_description(self):
        return self.description

    def re_number(self):
        return self.number
