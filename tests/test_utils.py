import pytest

from utils import *


@pytest.fixture  # ссылка с JSON, правильная структура
def link_good():
    return 'https://www.jsonkeeper.com/b/RRIL'


@pytest.fixture  # ссылка c JSON, правильная структура, но мало данных
def link_small_data():
    return 'https://www.jsonkeeper.com/b/ASZI'


@pytest.fixture  # ссылка c JSON, неправильная структура - dict
def link_dict_json():
    return 'https://www.jsonkeeper.com/b/Q1U0'


@pytest.fixture  # не JSON
def link_improper():
    return 'https://google.ru'


@pytest.fixture  # нерабочая ссылка
def error_link():
    return 'https://jsonkeeper.com/b/RRIL'


@pytest.fixture  # то, что должно получиться при правильной работе
def selected_good():
    return 'https://www.jsonkeeper.com/b/3S1E'


@pytest.fixture  # маскируем карту
def card():
    return 'Maestro 1596837868705199'


@pytest.fixture  # маскируем счет
def account():
    return 'Счет 64686473678894779589'


def test_load_json(link_good, link_improper, error_link, link_small_data, link_dict_json):
    assert load_json(link_good) is not None
    assert load_json(link_small_data) is not None
    assert load_json(link_dict_json) is None
    assert load_json(link_improper) is None
    assert load_json(error_link) is None


def test_select(link_good, selected_good, link_small_data, link_dict_json):
    assert select(load_json(link_good), 5) == load_json(selected_good)
    assert select(load_json(link_small_data), 5) is None


def test_to_mask(card, account):
    assert to_mask(card) == 'Maestro 1596 83** **** 5199'
    assert to_mask(account) == 'Счет **9589'
