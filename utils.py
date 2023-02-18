from json import dumps
from re import fullmatch, search
from requests import get
from datetime import datetime


def load_json(link: str):
    """Загружает JSON с указанного url"""
    try:  # пробует загрузить JSON
        data = get(link).json()
    except Exception:
        return None  # возвращает None в случае любой ошибки
    else:
        return data  # возвращает результат, если удалось загрузить


def operation_check(operation: dict) -> bool:
    """Проверяет операцию на соответствие шаблону"""
    op_str = dumps(operation, ensure_ascii=False)  # преобразует словарь в строку
    # определяет шаблон для проверки структуры операции
    regex = r'{"id": \d+, "state": "EXECUTED", "date": "\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}", ' \
            r'"operationAmount": {"amount": "\d*\.?\d*", "currency": {"name": ".+", "code": ".+"}}, ' \
            r'"description": ".+", "from": ".+ (\d{16}|\d{20})", "to": ".+ (\d{16}|\d{20})"}'
    # возвращает True при совпадении операции с шаблоном, иначе False
    return True if fullmatch(regex, op_str) else False


def select(data: list[dict], num: int) -> list[dict] | None:
    """Возвращает подходящие по шаблону, отсортированные по полю 'date', данные в нужном количестве, если их есть"""
    operations = list(filter(operation_check, data))  # фильтрует соответствующие шаблону словари
    if len(operations) >= num:  # если данных достаточно, сортирует по полю 'date' и возвращает
        return list(sorted(operations, key=lambda x: x['date'], reverse=True))[:num]
    else:
        return None


def to_mask(data: str) -> str:
    """Маскирует номер карты или счета"""
    regex = r'\b\d{16}\b|\b\d{20}\b'  # определяет шаблон из 16ти или 20ти цифр
    num = search(regex, data).group()  # получает номер карты или счета
    name = data.removesuffix(num)  # получает название карты или "Счет"
    # маскирует номер карты или счета
    num = '**' + num[16:20] if len(num) == 20 else num[0:4] + ' ' + num[4:6] + '** ' + '**** ' + num[12:16]
    return name + num


def operation_display(data: dict) -> None:
    """Форматированный вывод операции"""
    date = datetime.fromisoformat(data['date'])  # преобразует str в date для удобства работы
    # выводит данные по операции в нужном формате
    print(f"{date.day}.{date.month}.{date.year} {data['description']}\n"
          f"{to_mask(data['from'])} -> {to_mask(data['to'])}\n"
          f"{data['operationAmount']['amount']} {data['operationAmount']['currency']['name']}\n")
