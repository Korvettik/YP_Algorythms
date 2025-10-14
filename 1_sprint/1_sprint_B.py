# https://contest.yandex.ru/contest/22450/run-report/144286156/

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
    return matrix, k


def get_maximum_score(matrix, k):
    """функция основной логики"""
    maximum_score = 0
    max_buttons = k * 2

    matrix_dict = {'1': 0,
                   '2': 0,
                   '3': 0,
                   '4': 0,
                   '5': 0,
                   '6': 0,
                   '7': 0,
                   '8': 0,
                   '9': 0,
                   }

    for button in matrix:
        if button != '.':
            matrix_dict[button] += 1

    #print(f'matrix_dict {matrix_dict}')

    for k, v in matrix_dict.items():
        if v <= max_buttons and v != 0:
            maximum_score += 1


    return maximum_score



matrix, k = read_input()
print(get_maximum_score(matrix, k))
