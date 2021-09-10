"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    class_list = [
        {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
        {'school_class': '4b', 'scores': [5, 4, 3, 3, 5, 3]},
        {'school_class': '4c', 'scores': [3, 2, 5, 2, 2]}
    ]

    class_score_count = 0
    class_score_sum = 0
    school_score_count = 0
    school_score_sum = 0
    for klass in class_list:
        for score in klass['scores']:
            class_score_sum += score
            class_score_count += 1
        print('Средняя оценка по классу ' + klass['school_class'] + ' ' + str(
            round(class_score_sum / class_score_count, 2)))
        school_score_sum = school_score_sum + class_score_sum
        school_score_count = school_score_count + class_score_count
        class_score_sum = 0
        class_score_count = 0
    print(f'Средняя оценка по школе {round(school_score_sum / school_score_count, 2)}')


if __name__ == "__main__":
    main()
