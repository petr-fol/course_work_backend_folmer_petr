class Receipt:
    """
    Представляет чек с различными атрибутами, такими как идентификатор, состояние, дата,
    сумма, валюта, описание, отправитель и получатель.
    """

    def __init__(self, id_, state_, date_, amount_=None, name_=None,
                 code_=None, description_=None, from_=None, to_=None, date_value_=None):
        """
        Инициализирует объект Receipt с заданными атрибутами.

        Аргументы:
            id_ (str): Идентификатор чека.
            state_ (str): Состояние чека.
            date_ (str): Дата чека.
            amount_ (float, optional): Сумма чека. По умолчанию None.
            name_ (str, optional): Название валюты. По умолчанию None.
            code_ (str, optional): Код валюты. По умолчанию None.
            description_ (str, optional): Описание чека. По умолчанию None.
            from_ (str, optional): Отправитель чека. По умолчанию None.
            to_ (str, optional): Получатель чека. По умолчанию None.
            date_value_ (str, optional): Контрольная сумма для сортировки чеков. По умолчанию None.
        """

        self.id = id_
        self.state = state_
        self.date = date_
        self.amount = amount_
        self.currency = name_
        self.currency_code = code_
        self.description = description_
        self.sender = from_
        self.recipient = to_
        self.date_value = date_value_

    def __str__(self):
        """
        Возвращает строковое представление объекта Receipt.

        Returns:
            str: Строковое представление объекта Receipt.
        """
        return (f'Чек {self.id} от {self.sender}'
                f' к {self.recipient}'
                f' на сумму {self.amount} {self.currency}')

    def __repr__(self):
        """
        Возвращает строковое представление объекта Receipt.

        Returns:
            str: Строковое представление объекта Receipt.
        """
        return (f'Чек {self.id} от {self.sender}'
                f' к {self.recipient}'
                f' на сумму {self.amount} {self.currency}')

    def re_id(self):
        """
        Возвращает идентификатор чека.

        Returns:
            str: Идентификатор чека.
        """
        return self.id

    def re_state(self):
        """
        Возвращает состояние чека.

        Returns:
            str: Состояние чека.
        """
        return self.state

    def re_date(self):
        """
        Возвращает дату чека.

        Returns:
            str: Дата чека.
        """
        return self.date

    def re_amount(self):
        """
        Возвращает сумму чека.

        Returns:
            float: Сумма чека.
        """
        return self.amount

    def re_currency(self):
        """
        Возвращает название валюты чека.

        Returns:
            str: Название валюты чека.
        """
        return self.currency

    def re_currency_code(self):
        """
        Возвращает код валюты чека.

        Returns:
            str: Код валюты чека.
        """
        return self.currency_code

    def re_description(self):
        """
        Возвращает описание чека.

        Returns:
            str: Описание чека.
        """
        return self.description

    def re_sender(self):
        """
        Возвращает отправителя чека.

        Returns:
            str: Отправитель чека.
        """
        return self.sender

    def re_recipient(self):
        """
        Возвращает получателя чека.

        Returns:
            str: Получатель чека.
        """
        return self.recipient
