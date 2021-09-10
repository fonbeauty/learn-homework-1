"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""


def hello_user():
    """
    Замените pass на ваш код
    """
    # def hello_user():
    while True:
        try:
            user_input = input('Как дела? ')
            if user_input.lower() == 'хорошо':
                print('Пока!')
                break
        except KeyboardInterrupt:
            print()
            print('Пока!')
            break


hello_user()
