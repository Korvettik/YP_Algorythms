# https://contest.yandex.ru/contest/22450/run-report/144633672/

# from collections import defaultdict


class Data:
    def __str__(self):
        """класс хранения данных"""

    def __init__(self):
        self.matrix = None
        self.k = None

def read_input():
    """получаем данные задачи из стандартного ввода"""
    k = int(input())
    #matrix = []
    matrix = ''
    for _ in range(4):
        #matrix.append(input().strip())
        matrix += input().strip()

    return matrix, k


def get_maximum_score(matrix, k):
    """функция основной логики"""

    maximum_score = 0
    max_buttons = k * 2

    # # Создание defaultdict с типом данных по умолчанию
    # matrix_dict = defaultdict(int)  # int() по умолчанию вернет в ключе 0

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


    # for button in matrix:
    #     if button != '.':
    #         matrix_dict[button] += 1
    #
    #
    # for k, v in matrix_dict.items():
    #     if v <= max_buttons and v != 0:
    #         maximum_score += 1


    matrix_list = [0] * 10  # список, где индексы будут как-бы ключами, а элементы списка - значениями

    for button in matrix:
        if button != '.':
            matrix_list[int(button)] += 1

    for v in matrix_list:
        if v <= max_buttons and v != 0:
            maximum_score += 1

    return maximum_score



if __name__ == '__main__':
    # создаем объект хранения данных
    data = Data()

    # теперь храним данные в объекте
    data.matrix, data.k = read_input()

    print(get_maximum_score(data.matrix, data.k))
