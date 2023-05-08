from utils.loaders import load_operations, load_executed_operations


def test_load_operations():
    """Тестирует загрузку данных из файла "operations.json":
    сравнивает длину полученного словаря и
    несколько элементов полученного словаря
    """
    expected_dict_1 = {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}
    expected_dict_2 = {'id': 667307132, 'state': 'EXECUTED', 'date': '2019-07-13T18:51:29.313309', 'operationAmount': {'amount': '97853.86', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с карты на счет', 'from': 'Maestro 1308795367077170', 'to': 'Счет 96527012349577388612'}
    expected_dict_12 = {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689', 'operationAmount': {'amount': '67314.70', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Visa Platinum 1246377376343588', 'to': 'Счет 14211924144426031657'}

    loaded_operations = load_operations('../operations.json')
    assert len(loaded_operations) == 101

    assert loaded_operations[0] == expected_dict_1
    assert loaded_operations[12] == expected_dict_12
    assert loaded_operations[-1] == expected_dict_2


def test_load_executed_operations():
    """Тестирует получение списка словарей с выполненными операциями:
    сравнивает длину полученного списка и
    несколько элементов полученного списка"""
    loaded_executed_operations = load_executed_operations('../operations.json')
    expected_dict_1 = {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}
    expected_dict_2 = {'id': 667307132, 'state': 'EXECUTED', 'date': '2019-07-13T18:51:29.313309', 'operationAmount': {'amount': '97853.86', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с карты на счет', 'from': 'Maestro 1308795367077170', 'to': 'Счет 96527012349577388612'}
    expected_dict_12 = {'id': 147815167, 'state': 'EXECUTED', 'date': '2018-01-26T15:40:13.413061', 'operationAmount': {'amount': '50870.71', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с карты на счет', 'from': 'Maestro 4598300720424501', 'to': 'Счет 43597928997568165086'}

    assert len(loaded_executed_operations) == 85

    assert loaded_executed_operations[0] == expected_dict_1
    assert loaded_executed_operations[12] == expected_dict_12
    assert loaded_executed_operations[-1] == expected_dict_2
