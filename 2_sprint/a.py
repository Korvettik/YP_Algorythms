class Data:
    def __str__(self):
        """класс хранения данных"""

    def __init__(self):
        self.n = None
        self.m = None
        self.matrix = None


def read_input():
    """получаем данные задачи из стандартного ввода"""
    n = int(input())  # количество строк матрицы
    m = int(input())  # количество столбцов матрицы

    matrix = list()
    for _ in range(n):
        matrix += map(str, input().strip().split())

    #print(matrix)
    return n, m, matrix


def get_transformated_matrix(n, m, matrix):
    """функция основной логики"""
    tranformated_matrix = []  # результирующий список матрицы

    index_j= 0
    for i_m in range(m): # шаг по столбцам
        for j_n in range(n): # шаг по строкам
            index = i_m + index_j
            #print(f'index {index}')
            tranformated_matrix.append(matrix[index])
            #print(tranformated_matrix)
            index_j += m
        index_j = 0

    #print(tranformated_matrix)
    return tranformated_matrix


if __name__ == '__main__':

    # создаем объект хранения данных
    data = Data()

    # теперь храним данные в объекте
    data.n, data.m, data.matrix = read_input()

    transformated_matrix = get_transformated_matrix(data.n, data.m, data.matrix)

    # вывод распаковкой, визуальная матрица
    if data.n > 0 and data.m > 0:
        for i in range(0, data.n * data.m, data.n):
            print(*transformated_matrix[i:i+data.n])