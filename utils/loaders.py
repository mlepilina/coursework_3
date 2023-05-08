import json


def load_operations(path):
    '''Загружает список словарей с операциями из файла'''
    with open(path, mode='r', encoding='utf-8') as file:
        return json.load(file)


def load_executed_operations(path):
    '''Возвращает список словарей с выполненными операциями'''
    executed_operations = []
    operations = load_operations(path)
    key = "state"
    for operation in operations:
        if key in operation:
            if operation[key] == "EXECUTED":
                executed_operations.append(operation)

    return executed_operations
