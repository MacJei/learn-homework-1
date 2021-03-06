"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def check_age():
  
  while True:
    age = input('Введите, пожалуйста, Ваш возраст в числовом формате:')

    try:
      age = abs(int(age))
    except ValueError:
      print('Error! This is not integer number, try again.')
      continue
    else:
      return age


def main(age):

  if age <= 6:
    return f"Вам всего {age}. Вы, наверное, в данном возрасте должны учиться в детском саду"
  if 7 <= age <= 17:
    return f"Вам всего {age}. Вы, наверное, в данном возрасте должны учиться в школе"
  if 18 <= age <= 30:
    return f"Вам всего {age}. Вы, наверное, в данном возрасте должны учиться в ВУЗе"
  else:
    return f"Вам всего {age}. Вы, наверное, в данном возрасте должны работать"


if __name__ == "__main__":
    age_user = check_age()
    quest = main(age_user)
    print(quest)

