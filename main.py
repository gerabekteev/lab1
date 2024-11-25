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
    if file_format == 'json':
        filename = 'data.json'
        data = js.load_from_json(filename)
        handler = js
        # elif file_format == 'xml':
        #     filename = 'data.xml'
        #     data = xm.load_from_xml(filename)
        #     handler = xm
        # else:
        print("Неверный формат!")
        return

    counter = 0

    while True:

        print("\nВыберите действие:")
        print("1 - Добавить одноразовый билет")
        print("2 - Добавить многоразовый билет")
        print("3 - Добавить подписочный билет")
        print("4 - Добавить льготный билет")
        print("5 - Удалить фильм")
        print("6 - Удалить сериал")
        print("7 - Удалить сериал")
        print("8 - Удалить сериал")
        print("10 - Сохранить")
        print("11 - Выход")
        print("12 - Сравнить и синхронизировать JSON и XML")
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
            title = input("Введите название сериала: ")
            director = input("Введите режиссера сериала: ")
            year = get_year("Введите год выпуска сериала: ")
            seasons = get_positive_int("Введите количество сезонов: ")
            episodes = get_positive_int("Введите количество эпизодов: ")
            tvseries = TVSeries(title, director, year, seasons, episodes)
            handler.add_tvseries(data, tvseries)

        elif action == '3':
            title = input("Введите название фильма для удаления: ")
            handler.delete_movie(data, title)

        elif action == '4':
            title = input("Введите название сериала для удаления: ")
            handler.delete_tvseries(data, title)

        elif action == '5':
            json_.save_to_json(data, filename_json)
            xml_.save_to_xml(data, filename_xml)
            print(f"Данные сохранены в {filename_json} и {filename_xml}")

        elif action == '6':
            break

        elif action == '7':
            json_data = json_.load_from_json('data.json')
            xml_data = xml_.load_from_xml('data.xml')
            sync_data(json_data, xml_data)
            json_.save_to_json(json_data, 'data.json')
            xml_.save_to_xml(xml_data, 'data.xml')
            print("Данные успешно синхронизированы и сохранены в оба файла.")
        elif action == '8':
            show_statistics(data)
        elif action == '999':
            PIZDEC(data)
        elif action == '13':
            try:
                if file_format != 'json':

                    raise InvalidFileFormatError("Неверный формат! Вы выбрали XML, а пытаетесь открыть JSON.")
                else:
                    filename = 'data.json'
                    data = json_.load_from_json(filename)
                    handler = json_
                    print_data(data, file_format)
            except InvalidFileFormatError as e:
                print(f"Ошибка: {e}")

        elif action == '169':
            try:
                if file_format != 'xml':
                    counter += 1
                    if counter == 1:
                        raise InvalidFileFormatError("Бывает, промахнулся, ничего страшного.")
                    elif counter == 2:
                        raise InvalidFileFormatError("Чумба, попей колесики.")
                    else:
                        raise InvalidFileFormatError(
                            "Ты меня пугаешь...неужели ты не понял что вообще нет смысла в разделении... и ничего мне не мешало немного изменить код? Я просто хотел хоть где то оставить свою лепту, ибо меняя названия переменных я бы потом вообще не понял, а где что....")
                else:
                    filename = 'data.xml'
                    data = xml_.load_from_xml(filename)
                    handler = xml_
                    print_data(data, file_format)
            except InvalidFileFormatError as e:
                print(f"{e}")

        else:
            print("Неверная команда!")


if __name__ == "__main__":
    main()
