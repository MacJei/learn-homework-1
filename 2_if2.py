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

def main(line_one, line_two):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    if not(isinstance(line_one, str) and isinstance(line_two, str)): # type(line_one) != str or type(line_two) != str
      return 0
    if line_one == line_two:
      return 1
    if len(line_one) > len(line_two):
        return 2
    if line_two == 'learn':
        return 3


if __name__ == "__main__":
    st1 = input('Введите значение: ')
    st2 = input('Введите значение: ')
    print(main(st1, st2))
    print(main(1, 'b'))
    print(main('learn', 'learn'))
    print(main('learn1', 'b'))
    print(main('1', 'learn'))
    print(main(1, [2]))