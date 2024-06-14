from datetime import datetime


class Operation:
    def __init__(
            self,
            date,
            state,
            amount,
            currency_name,
            description,
            from_account,
            to_account
    ):
        """
        Инициализация класса
        :param date:
        :param state:
        :param amount:
        :param currency_name:
        :param description:
        :param from_account:
        :param to_account:
        """
        self.date = date
        self.state = state
        self.amount = amount
        self.currency_name = currency_name
        self.description = description
        self.from_account = from_account
        self.to_account = to_account

    def get_iso_date(self):
        """
        Получает дату и возвращает её в формате ISO
        """
        return datetime.fromisoformat(self.date)

    def conversion_date(self):
        """
        Конвертирует дату к приведённому образцу дд.мм.ГГГГ
        :return:
        """
        iso_date = self.get_iso_date()
        return iso_date.strftime("%d.%m.%Y")
