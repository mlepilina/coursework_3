from _operator import itemgetter

from utils.loaders import load_executed_operations
from utils.operations import Operation


def create_result():
    """Записывает в список и возвращает 5 последних выполненных
    операций в правильном виде, необходимых для вывода
    """
    list_of_operations = load_executed_operations('../operations.json')
    list_of_operations.sort(key=itemgetter('date'), reverse=True)

    result = []

    for operation_dict in list_of_operations[:5]:
        operation = Operation(
            operation_dict['date'],
            operation_dict['to'],
            from_number=operation_dict.get('from', "Номер отправителя не указан"),
        )

        result.append(
            (
                f'{operation.build_date()} Перевод организации',
                f'{operation.build_hidden_number_from()} -> {operation.build_hidden_number_to()}',
                f'{operation_dict["operationAmount"]["amount"]} {operation_dict["operationAmount"]["currency"]["name"]}',
                ''
            )
        )

    return result
