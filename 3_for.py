from random import randint

def first_task():
  list_ = [randint(0,50) for _ in range(10)]
  list__ = []

  for i in list_:
    list__.append(i)

  print(list__)


def second_task():
  string = str(input('Введите слово: '))

  for word in string:
    print(word)

"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
def school_data():
  s = 'абвгдежзик'
  data = list()
  for i in range(12):
    data.append({
      'school_class': str(i + 1) + s[randint(0, len(s) - 1)],
      'scores': [randint(2,5) for _ in range(randint(3,19))]
    })

  return data


def main():
  data = school_data()
  #print(data)
  #print(len(data))
  avg_score_school = 0
  
  for clas in data:
    avg_score_class = sum(clas['scores']) / len(clas['scores'])
    clas_ = clas['school_class']
    print(f'Средний балл класса {clas_} равен {round(avg_score_class, 1)}')
    avg_score_school += avg_score_class / len(data)
  print(f'Средний балл по школе равен {round(avg_score_school, 1)}')
       
if __name__ == "__main__":
    main()
#   first_task()
#   second_task()
#   print(school_data())