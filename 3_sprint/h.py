from functools import cmp_to_key
# Класс cmp_to_key() модуля functools преобразует функцию
# сравнения старого стиля в ключевую функцию сравнения.


def comparator(a, b):
    """Функция сравнения - это любой вызываемый объект,
    который принимает два аргумента, сравнивает их и
    возвращает отрицательное число для "меньше чем",
    ноль для равенства значений и положительное число
    для "больше чем". Функция, используемая в качестве
    ключа - это вызываемый объект, который принимает
    один аргумент и возвращает другое значение, которое
    будет использоваться в качестве ключа сортировки."""

    if int(a + b) > int(b + a):   # 1 10   >  10 1   или 9 98  >  98 9
        return 1

    if int(a + b) < int(b + a):
        return -1

    return 0


def make_big_number(n, numbers_list):
    #print(numbers_list)
    numbers_list.sort(
                      reverse=True,
                      key=cmp_to_key(comparator)
                      )
    #print(numbers_list)

    print(int(''.join(numbers_list)))



n = int(input().strip())  # количество чисел
numbers_list = input().strip().split()  # список с числами (строки)

make_big_number(n, numbers_list)