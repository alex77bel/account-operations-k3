from utils import *

LINK = 'https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1676754812730&signature=Vq5aM5fl6l_X4e3nYQKjY-vunBOq1NCY1nl5I2OtvCA&downloadName=operations.json'

OPERATIONS_NUM = 5


def main():
    operations_loaded = load_json(LINK)  # загружает JSON
    if not operations_loaded:  # в случае неудачи завершает работу
        print('Не удалось загрузить данные с указанного адреса')
        return
    # выбирает операции, удовлетворяющие требованиям условия
    operations = select(operations_loaded, OPERATIONS_NUM)
    if not operations:  # в случае неудачи завершаем работу
        print('Недостаточно данных')
        return
    # выводит результат
    [operation_display(i) for i in operations]


if __name__ == "__main__":
    main()
