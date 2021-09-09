"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    def string_compare(string1, string2):
        if type(string1) != str or type(string2) != str:
            return 0
        elif string1 == string2:
            return 1
        elif len(string1) > len(string2):
            return 2
        elif string1 != string2 and string2 == "learn":
            return 3
        else:
            return -1

    print("Один из параметров не строка:", string_compare(1, "text"))
    print("Две одинаковые строки:", string_compare('text', "text"))
    print("Первая строка длиннее:", string_compare('text1', "text"))
    print("Вторая строка learn:", string_compare('text1', "learn"))
    print("Иначе:", string_compare('text', "text2"))


if __name__ == "__main__":
    main()
