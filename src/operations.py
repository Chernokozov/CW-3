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

    def masking_payment_information(self, payment_info, from_account=""):
        """
        Получает и маскирует платёжную информацию
        :param payment_info:
        :param from_account:
        :return:
        """
        if len(payment_info) > 6:
            if payment_info.startswith("Счет"):
                masked_part = payment_info[:4] + " **" + payment_info[-4:]
                return masked_part
            else:
                masked_part_2 = payment_info[:-12] + " " + payment_info[-12:-10] + "** **** " + payment_info[-4:]
                return masked_part_2

        return from_account

    def __gt__(self, other):
        """
        Сравнивает даты операций
        :param other:
        :return:
        """
        return self.get_iso_date() > other.get_iso_date()

    def __lt__(self, other):
        """
        Сравнивает даты операций
        :param other:
        :return:
        """
        return self.get_iso_date() < other.get_iso_date()

    def __str__(self):
        """
        Выводит пользовательскую информацию в заданном виде
        :return:
        """
        date = self.conversion_date()
        from_ = self.masking_payment_information(self.from_account)
        to = self.masking_payment_information(self.to_account)

        return (
            f"{date} {self.description}\n"
            f"{from_} -> {to}\n"
            f"{self.amount} {self.currency_name}\n"
        )
