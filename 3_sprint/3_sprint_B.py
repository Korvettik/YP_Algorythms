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


# быстрая сортировка
def partition(array, pivot):
    left = [x for x in array if x < pivot]
    center = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return left, center, right

def quicksort(array):
    if len(array) < 2:
        return array   # массивы с 0 или 1 элементами фактически отсортированы
    else:
        pivot = random.choice(array)
        left, center, right = partition(array, pivot)
        return quicksort(left) + center + quicksort(right)



if __name__ == '__main__':
    n = int(input().strip())  # число участников

    user_list = list()
    for user in range(n):
        user_list.append(input().strip().split())  # читаем параметры пользователя

    print(user_list)