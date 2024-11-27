import js
import xm
from my_class import one_time, many_time, subscription, preferential
from datetime import datetime


def is_date_in_range(temp, start_date, end_date):
    date_format = "%d.%m.%Y"
    """
    Проверяет корректность даты и входит ли она в заданный временной промежуток.

    :param date_str: Введенная дата в виде строки.
    :param date_format: Формат даты (например, "%d.%m.%Y").
    """
    while True:
        date_str = input(temp)
        try:
            input_date = datetime.strptime(date_str, date_format)
            # Проверяем, входит ли дата в промежуток
            if start_date <= input_date <= end_date:
                return date_str
            else:
                print("Дата не входит в указанный промежуток.")
        except ValueError:
            print("Некорректный формат даты!",date_format)


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
            col_use = positiv_number("введите количество использований: ")
            exp = many_time(name_owner, transport, cl, time_ti_buy,price,col_use)
            handler.add_many_time(data, exp)

        elif action == '3':
            name_owner = input("Введите имя владельца: ")
            transport = input("Введите тип транспорта: ")
            cl = input("Введите класс билета: ")
            time_ti_buy = is_date_in_range("Введите дату оформления: ", start_date, end_date)
            price = positiv_number("Введите цену: ")
            col_day = positiv_number("введите количество дней: ")
            exp = subscription(name_owner, transport, cl, time_ti_buy,price,col_day)
            handler.add_subscription(data, exp)

        elif action == '4':
            name_owner = input("Введите имя владельца: ")
            transport = input("Введите тип транспорта: ")
            cl = input("Введите класс билета: ")
            time_ti_buy = is_date_in_range("Введите дату оформления: ", start_date, end_date)
            reason = input("введите причину выдачи: ")
            exp = preferential(name_owner, transport, cl, time_ti_buy,0,reason)
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

        elif action == '13':
            print("один -", len(data["one_time"]))
            print("много -",len(data["many_time"]))
            print("подписка -",len(data["subscription"]))
            print("льгота -",len(data["preferential"]))
        elif action == '14' or action == "15":
            if action=="14":
                data_temp = js.load_from_json(filename_json)
            else:
                data_temp = xm.load_from_xml(filename_xml)
            try:
                print("одноразовые:")
                for exp in data_temp['one_time']:
                    print(f"имя: {exp['name_owner']}, транспорт: {exp['transport']}, "
                          f"класс: {exp['cl']}, время покупки: {exp['time_ti_buy']}, "
                          f"цена: {exp['price']}")
            except KeyError:
                print("пусто")
            try:
                print("--------------------------")
                print("многоразовый:")
                for exp in data_temp['many_time']:
                    print(f"имя: {exp['name_owner']}, транспорт: {exp['transport']}, "
                          f"класс: {exp['cl']}, время покупки: {exp['time_ti_buy']}, "
                          f"цена: {exp['price']}, количество использований: {exp['col_use']}")
            except KeyError:
                print("пусто")
            try:
                print("--------------------------")
                print("подписочный:")
                for exp in data_temp['subscription']:
                    print(f"имя: {exp['name_owner']}, транспорт: {exp['transport']}, "
                            f"класс: {exp['cl']}, время покупки: {exp['time_ti_buy']}, "
                            f"цена: {exp['price']}, количество дней: {exp['col_day']}")
            except KeyError:
                print("Пусто")
            try:
                print("--------------------------")
                print("льготный:")
                for exp in data_temp['preferential']:
                    print(f"имя: {exp['name_owner']}, транспорт: {exp['transport']}, "
                          f"класс: {exp['cl']}, время покупки: {exp['time_ti_buy']}, "
                          f"цена: {exp['price']}, причина: {exp['reason']}")
            except KeyError:
                print("пусто")


        else:
            print("несуществующая команда")


if __name__ == "__main__":
    main()
