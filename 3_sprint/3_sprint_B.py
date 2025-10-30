#

# -- ПРИНЦИП РАБОТЫ ---


# -- ДОКАЗАТЕЛЬСТВА КОРРЕКТНОСТИ --

# -- ОПРЕДЕЛЕНИЕ СЛОЖНОСТИ АЛГОРИТМА --


import random

# ваша реализация сортировки не может потреблять O(n) дополнительной памяти для промежуточных
# данных (такая модификация быстрой сортировки называется "in-place").

# при сравнении двух участников выше будет идти тот, у которого решено больше задач.
# При равенстве числа решённых задач первым идёт участник с меньшим штрафом.
# Если же и штрафы совпадают, то первым будет тот, у которого логин идёт раньше в алфавитном (лексикографическом) порядке.


# # быстрая сортировка
# def partition(array, pivot):
#     left = [x for x in array if x < pivot]
#     center = [x for x in array if x == pivot]
#     right = [x for x in array if x > pivot]
#     return left, center, right
#
# def quicksort(array):
#     if len(array) < 2:
#         return array   # массивы с 0 или 1 элементами фактически отсортированы
#     else:
#         pivot = random.choice(array)
#         left, center, right = partition(array, pivot)
#         return quicksort(left) + center + quicksort(right)


# модицифицированная быстрая сортировка
def partition(array, pivot):
    """логика разделения списка на 2 части"""
    left = list()  # самые сильные
    center = list()
    right = list()  # самые слабые

    #print(f'pivot {pivot}')

    # слева будут лучшие, правее худшие
    for user in array:
        #print(f'user {user}')
        # сравнение по баллам
        if user[1] > pivot[1]:
            left.append(user)
        elif user[1] == pivot[1]:

            # сравнение по штрафам
            if user[2] > pivot[2]:
                left.append(user)
            elif user[2] == pivot[2]:

                # сравнение по имени
                if user[0] < pivot[0]:
                    left.append(user)
                elif user[0] == pivot[0]:
                    center.append(user)

                elif user[0] > pivot[0]:
                    right.append(user)


            elif user[2] < pivot[2]:
                right.append(user)

        elif user[1] < pivot[1]:
            right.append(user)

    return left, center, right


def quicksort(array):
    """общая логика + слияние"""
    #print(f'array {array}')

    # массивы с 0 или 1 элементами фактически отсортированы
    if len(array) < 2:
        #print(f'array {array}')
        return array
    else:
        pivot = random.choice(array)  # берем любого user
        left, center, right = partition(array, pivot)  # запускаем деление на 2 группы слева и справа
        return quicksort(left) + center + quicksort(right)  # обратным ходом склеиваем

if __name__ == '__main__':
    n = int(input().strip())  # число участников

    user_list = list()
    for user in range(n):
        user_list.append(input().strip().split())  # читаем параметры пользователя

    #print(user_list)

    #print(*quicksort(user_list), sep='\n')

    print(*list(item[0] for item in quicksort(user_list)), sep='\n')
