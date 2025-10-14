# https://contest.yandex.ru/contest/22450/run-report/144631204/


class Data:
    def __str__(self):
        """класс хранения данных"""

    def __init__(self):
        self.property_indexes = None
        self.n = None




def read_input():
    """получаем данные задачи из стандартного ввода"""
    n = int(input())
    property_indexes = list(map(int, input().strip().split()))
    return property_indexes, n


def get_property_distances(property_indexes, n):
    """функция основной логики"""

    # 1 вариант, медленный ========================================================

    # property_distances = []
    # zero_indexes = []
    # for i in range(n):
    #     if property_indexes[i] == 0:  # свободный участок сам по себе
    #         zero_indexes.append(i)
    # # уже знаем индексы пустых участков
    # for i in range(n):
    #     if property_indexes[i] == 0:
    #         property_distances.append(0)
    #     else:
    #         # находим минимальную разницу между текущим индексом и известным нулевым
    #         distance_list = []
    #         for zero_index in zero_indexes:
    #             distance = abs(i - zero_index)
    #             distance_list.append(distance)
    #         property_distances.append(min(distance_list))





    # 2 вариант, скоростной ======================================================

    property_distances = [0] * n  # результирующие расстояния по умолчанию все в 0
    #print(property_distances)
    last_zero_i = None

    for i in range(n):  # проходим список слева направо
        if property_indexes[i] == 0:
            last_zero_i = i

        if last_zero_i is None:  # пока не встретился
            property_distances[i] = n  # просто максимальное значение
        else:
            property_distances[i] = abs(i - last_zero_i)

    for i in range(n)[::-1]:  # проходим в обратном порядке, но уже по полученным расстояниям
        if property_distances[i] == 0:  # тут так и останется от первого прогона
            last_zero_i = i

        new_distance = abs(i - last_zero_i)
        if property_distances[i] > new_distance:  # сам элемент уже расстояние при первом прогоне
            property_distances[i] = new_distance

    return property_distances





if __name__ == '__main__':
    # создаем объект хранения данных
    data = Data()

    # теперь храним данные в объекте
    data.property_indexes, data.n = read_input()

    # вывод распаковкой
    print(*get_property_distances(data.property_indexes, data.n))
