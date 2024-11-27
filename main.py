import js
import xm
from my_class import one_time, many_time, subscription, preferential
from datetime import datetime


def is_date_in_range(temp, start_date, end_date):
    date_format = "%Y-%m-%d"
    """
    Проверяет корректность даты и входит ли она в заданный временной промежуток.

    :param date_str: Введенная дата в виде строки.
    :param date_format: Формат даты (например, '%Y-%m-%d').
    """
    while True:
        date_str = input(temp)
        try:
            input_date = datetime.strptime(date_str, date_format)
            # Проверяем, входит ли дата в промежуток
            if start_date <= input_date <= end_date:
                return date_str
            else:
                return "Дата не входит в указанный промежуток."
        except ValueError:
            return False, "Некорректный формат даты!"


def positiv_number(temp):
    while True:
        try:
            num = int(input(temp))
            if num >= 0:
                return num
            else:
                print("введите положительное число")
        except ValueError:
            print("Поддерживаются только числа")
        else:
            print("введите положительное число")


def main():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 12, 31)

    print("json / xml -")
    file_format = input().lower()
    filename_json = 'data.json'
    filename_xml = 'data.xml'
    if file_format == 'json':
        filename = 'data.json'
        data = js.load_from_json(filename)
        handler = js
    elif file_format == 'xml':
        filename = 'data.xml'
        data = xm.load_from_xml(filename)
        handler = xm
    else:
        print("Неверный формат!")
        return

    counter = 0

    while True:

        print("Выберите действие:")
        print("1 - Добавить одноразовый билет")
        print("2 - Добавить многоразовый билет")
        print("3 - Добавить подписочный билет")
        print("4 - Добавить льготный билет")
        print("5 - Удалить одноразовый билет")
        print("6 - Удалить  многоразовый билет")
        print("7 - Удалить подписочный билет")
        print("8 - Удалить льготный билет")
        print("10 - Сохранить")
        print("11 - Выход")
        print("13 - Статистика по БД")
        print("14 - Вывести данные из JSON")
        print("15 - Вывести данные из XML")

        action = input()
        """
        1 - готовое действие остальные переписать по образу и пожобию
        остальные функции и xml
        
        """
        if action == '1':
            name_owner = input("Введите имя владельца: ")
            transport = input("Введите тип транспорта: ")
            cl = input("Введите класс билета: ")
            time_ti_buy = is_date_in_range("Введите дату оформления: ",start_date,end_date)
            price = positiv_number("Введите цену: ")
            exp = one_time(name_owner, transport, cl, time_ti_buy,price)
            handler.add_one_time(data, exp)

        elif action == '2':
            name_owner = input("Введите имя владельца: ")
            transport = input("Введите тип транспорта: ")
            cl = input("Введите класс билета: ")
            time_ti_buy = is_date_in_range("Введите дату оформления: ", start_date, end_date)
            price = positiv_number("Введите цену: ")
            col_use = positiv_number("введите количество использований:")
            exp = many_time(name_owner, transport, cl, time_ti_buy,price,col_use)
            handler.add_many_time(data, exp)

        elif action == '3':
            name_owner = input("Введите имя владельца: ")
            transport = input("Введите тип транспорта: ")
            cl = input("Введите класс билета: ")
            time_ti_buy = is_date_in_range("Введите дату оформления: ", start_date, end_date)
            price = positiv_number("Введите цену: ")
            col_day = positiv_number("введите количество дней:")
            exp = many_time(name_owner, transport, cl, time_ti_buy,price,col_day)
            handler.add_subscription(data, exp)

        elif action == '4':
            name_owner = input("Введите имя владельца: ")
            transport = input("Введите тип транспорта: ")
            cl = input("Введите класс билета: ")
            time_ti_buy = is_date_in_range("Введите дату оформления: ", start_date, end_date)
            #price = positiv_number("Введите цену: ")
            reason = input("введите причину выдачи")
            exp = many_time(name_owner, transport, cl, time_ti_buy,0,reason)
            handler.add_preferential(data, exp)

        elif action == '5':
            title = input("Введите имя владельца для удаления: ")
            handler.delete_one_time(data, title)
        elif action == '6':
            title = input("Введите имя владельца для удаления: ")
            handler.delete_many_time(data, title)
        elif action == '7':
            title = input("Введите имя владельца для удаления: ")
            handler.delete_subscription(data, title)
        elif action == '8':
            title = input("Введите имя владельца для удаления: ")
            handler.delete_preferential(data, title)

        elif action == '10':
            js.save_to_json(data, filename_json)
            xm.save_to_xml(data, filename_xml)
            print(f"Данные сохранены в {filename_json} и {filename_xml}")

        elif action == '11':
            break

        # elif action == '12':
        #     json_data = js.load_from_json('data.json')
        #     xml_data = xm.load_from_xml('data.xml')
        #     sync_data(json_data, xml_data)
        #     js.save_to_json(json_data, 'data.json')
        #     xm.save_to_xml(xml_data, 'data.xml')
        #     print("Данные успешно синхронизированы и сохранены в оба файла.")
        elif action == '13':
            print("один -", len(data["one_time"]))
            print("много -",len(data["many_time"]))
            print("подписка -",len(data["subscription"]))
            print("льгота -",len(data["preferential"]))
        # elif action == '999':
        #     PIZDEC(data)
        elif action == '14':
            print("одноразовый:")
            for exp in data['one_time']:
                print(f"имя: {exp['name_owner']}, транспорт: {exp['transport']}, "
                      f"класс: {exp['cl']}, время покупки: {exp['time_ti_buy']},"
                      f"цена: {exp['price']}")

            print("многоразовый:")
            for exp in data['one_time']:
                print(f"имя: {exp['name_owner']}, транспорт: {exp['transport']}, "
                      f"класс: {exp['cl']}, время покупки: {exp['time_ti_buy']},"
                      f"цена: {exp['price']},количество использований: {exp['col_use']}")
            print("подписочный:")
            for exp in data['one_time']:
                print(f"имя: {exp['name_owner']}, транспорт: {exp['transport']}, "
                      f"класс: {exp['cl']}, время покупки: {exp['time_ti_buy']},"
                      f"цена: {exp['price']},количество дней: {exp['col_day']}")
            print("льготный:")
            for exp in data['one_time']:
                print(f"имя: {exp['name_owner']}, транспорт: {exp['transport']}, "
                      f"класс: {exp['cl']}, время покупки: {exp['time_ti_buy']},"
                      f"цена: {exp['price']},причина: {exp['reason']}")


        else:
            print("Неверная команда!")


if __name__ == "__main__":
    main()
