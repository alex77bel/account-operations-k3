# Курсовой проект по курсу «Основы backend-разработки»
## Код для виджета «Операции по счетам»
IT-отдел крупного банка делает новую фичу для личного кабинета клиента. Это виджет, который показывает несколько последних успешных банковских операций клиента. 
Вам доверили реализовать алгоритм, который на бэкенде будет готовить данные для отображения в новом виджете.
## Задача
Реализуйте функцию, которая выводит на экран список из 5 последних выполненных клиентом операций в формате:
- <дата перевода> <описание перевода>
- <откуда> -> <куда>
- <сумма перевода> <валюта>

**Проект состоит из файлов:** 
- main.py – содержит константы, главную функцию
- utils.py – содержит следующие функции:
load_json - загружает JSON с указанного url.
operation_check - проверяет операцию на соответствие шаблону
select – возвращает данные, подходящие по шаблону, отсортированные по дате, в заданном количестве
mask - маскирует номер карты или счета
operation_display - форматированный вывод операции

Алгоритм работы.
1. Исходные данные – ссылка на список операций, количество выводимых операций.
2. Функция load_json получает на вход ссылку, пробует загрузить список, в случае ошибки загрузки или декодирования JSON возвращает None 
(и выводится сообщение об ошибке), в удачном случае – данные для дальнейшей обработки.
3. Функция select получает на вход загруженные данные и количество выводимых операций.
Данные фильтруются поэлементно на соответствие шаблонной строке (функция operation_check). В случае, если находится достаточное количество записей,
удовлетворяющих шаблону, они возвращаются функцией, в противном случае возвращается None и сообщение "Недостаточно данных".
4. В конце выводятся выбранные операции (функция operation_display), в требуемом формате.
