# Выведите через пробел k ID вузов с максимальным числом участников.
# Они должны быть отсортированы по убыванию популярности (по количеству
# гостей от конкретного вуза).
# Если более одного вуза имеет одно и то же
# количество учащихся, то выводить их ID нужно в порядке возрастания.

def find_students(n, id_list, k):
    #print(n, id_list, k)
    # id_list.sort()
    id_dict = dict()
    for id in id_list:
        if id not in id_dict.keys():
            id_dict[id] = 1
        else:
            id_dict[id] += 1
    #print(id_dict)

    id_tuple = list(id_dict.items())

    # -item[1] - сортировка по убыванию количества
    # (используем отрицательное значение для убывающей сортировки)

    # item[0] - сортировка по возрастанию ID

    id_tuple.sort(
        reverse=True,  # (3) разворачиваем сортировку
        key=lambda item: (item[1], -item[0])  # (1) по возрастанию,  (2) по убыванию
        )
    # print(id_tuple)




    result = []
    #print(id_tuple)
    for i in range(k):
        if i < len(id_tuple):
            result.append(id_tuple[i][0])

    print(*result, sep=' ')


n = int(input().strip())  #  количество студентов в списке
id_list = list(map(int, input().strip().split(' '))) #  ID вуза каждого студента
k = int(input())  # число самых встречающихся ID

find_students(n, id_list, k)
