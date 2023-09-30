class Receipt:
    def __init__(self, id_, state_, date_, amount_, name_, code_, description_, from_, to_):
        self.id = id_
        self.state = state_
        self.date = date_
        self.amount = amount_
        self.currency = name_
        self.currency_code = code_
        self.description = description_
        self.sender = from_
        self.recipient = to_

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
