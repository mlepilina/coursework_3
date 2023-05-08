from datetime import datetime


class Operation:
    def __init__(self, date, to_number, from_number):
        self.date = date
        self.from_number = from_number
        self.to_number = to_number

    def build_date(self):
        """Возвращает дату в в формате ДД.ММ.ГГГГ"""
        datetime_object = datetime.strptime(self.date, '%Y-%m-%dT%H:%M:%S.%f')
        valid_format = datetime_object.strftime('%d.%m.%Y')
        return valid_format

    def build_hidden_number_from(self):
        """Возвращает номер карты в формате  XXXX XX** **** XXXX"""
        list_from_card = self.from_number.split(' ')
        list_of_words = list_from_card[:-1]
        words = ' '.join(list_of_words)
        if list_from_card[-1].isdigit():
            number_of_card = list_from_card[-1]
            quarter_1 = number_of_card[:4]
            quarter_2 = number_of_card[4:6]+'**'
            quarter_3 = '****'
            quarter_4 = number_of_card[12:]
            return f'{words} {quarter_1} {quarter_2} {quarter_3} {quarter_4}'
        else:
            return self.from_number

    def build_hidden_number_to(self):
        """Возвращает счет получателя в формате  **XXXX """
        list_to_card = self.to_number.split(' ')
        list_of_words = list_to_card[:-1]
        words = ' '.join(list_of_words)
        number = list_to_card[-1]
        last_numbers = number[-4:]
        return f'{words} **{last_numbers}'

