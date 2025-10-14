#  https://contest.yandex.ru/contest/22450/run-report/144429034/


from collections import defaultdict


class Data:
    def __str__(self):
        """класс хранения данных"""

    def __init__(self):
        self.matrix = None
        self.k = None


data = Data()

def read_input():
    """получаем данные задачи из стандартного ввода"""
    k = int(input())
    #matrix = []
    matrix = ''
    for _ in range(4):
        #matrix.append(input().strip())
        matrix += input().strip()

    #print(f'k {k}')
    #print(f'matrix {matrix}')

    # теперь храним данные в объекте
    data.matrix = matrix
    data.k = k


def get_maximum_score():
    """функция основной логики"""

    # берем из объекта хранения
    k = data.k
    matrix = data.matrix

    maximum_score = 0
    max_buttons = k * 2

    # Создание defaultdict с типом данных по умолчанию
    matrix_dict = defaultdict(int)  # int() по умолчанию вернет в ключе 0

    # matrix_dict = {'1': 0,
    #                '2': 0,
    #                '3': 0,
    #                '4': 0,
    #                '5': 0,
    #                '6': 0,
    #                '7': 0,
    #                '8': 0,
    #                '9': 0,
    #                }

    for button in matrix:
        if button != '.':
            matrix_dict[button] += 1

    #print(f'matrix_dict {matrix_dict}')

    for k, v in matrix_dict.items():
        if v <= max_buttons and v != 0:
            maximum_score += 1


    return maximum_score



read_input()
print(get_maximum_score())
