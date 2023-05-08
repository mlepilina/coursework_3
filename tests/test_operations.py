from utils.operations import Operation


def test_operations():
    """Тестирует функции класса "Operation":
    вывод в нужный формат даты, счета отправителя
    и счета получаетеля
    """
    data = {
        'id': 441945886,
        'state': 'EXECUTED',
        'date': '2019-08-26T10:50:58.294041',
        'operationAmount': {
            'amount': '31957.58',
            'currency': {'name': 'руб.', 'code': 'RUB'}
        },
        'description': 'Перевод организации',
        'from': 'Maestro 1596837868705199',
        'to': 'Счет 64686473678894779589'
    }

    operation = Operation(data['date'], data['to'], data.get('from'))

    assert operation.build_date() == '26.08.2019'
    assert operation.build_hidden_number_from() == 'Maestro 1596 83** **** 5199'
    assert operation.build_hidden_number_to() == 'Счет **9589'
