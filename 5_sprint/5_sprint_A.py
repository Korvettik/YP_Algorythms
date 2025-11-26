#

# -- ПРИНЦИП РАБОТЫ ---



# -- ДОКАЗАТЕЛЬСТВА КОРРЕКТНОСТИ --



# -- ОПРЕДЕЛЕНИЕ СЛОЖНОСТИ АЛГОРИТМА --



def heapsort(array):
    # Создадим пустую бинарную кучу.
    heap = [None]

    # Вставим в неё по одному все элементы массива, сохраняя свойства кучи.
    for item in array:
        heap_add(heap, item)   # код для heap_add можно посмотреть в прошлом уроке

    # Будем извлекать из неё наиболее приоритетные элементы, удаляя их из кучи.
    sortedArray = []
    while len(heap) > 1:
        max_val = pop_max(heap)
        sortedArray.append(max_val)

    return sortedArray



def sift_up(heap, index):
    if index == 1:
        return

    parent_index = index // 2
    if heap[index] > heap[parent_index]:
        heap[index], heap[parent_index] = heap[parent_index], heap[index]
        sift_up(heap, parent_index)
#
#
def heap_add(heap, key):
    heap.append(key)
    index = len(heap)-1
    sift_up(heap, index)


def sift_down(heap, index):
    heap_max_index = len(heap)-1
    left = index*2
    right = index*2+1

    # нет дочерних узлов
    if left > heap_max_index:
        return

    # проверяем, что есть оба дочерних узла
    if right <= heap_max_index and heap[right] > heap[left]:
        index_largest = right
    else:
        index_largest = left
    # отправляем максимум на вершину кучи и рекурсивно завпускаем просеивание в ребенке
    if heap[index_largest] > heap[index]:
        heap[index_largest], heap[index] = heap[index], heap[index_largest]
        sift_down(heap, index_largest)
#
#
def pop_max(heap):
    result = heap[1]
    heap[1] = heap[len(heap) - 1]
    heap.pop()
    sift_down(heap, 1)
    return result








if __name__ == '__main__':

    if __name__ == '__main__':
        n = int(input().strip())  # число участников

        user_list = list()  # список с участниками

        for user in range(n):
            user_name, user_score, user_penalty = input().strip().split()  # читаем параметры пользователя
            # записываем в виде кортежа информацию о каждом пользователе

            # сравниваться будут кортежи, поэтому немного модифицируем порядок
            user_list.append((-int(user_score), int(user_penalty), user_name))  # записываем в виде кортежа информацию о каждом пользователе


        # print(user_list)
        # print(sorted(user_list))





        # запуск.
        sorted_user_list = heapsort(user_list)





        # Вывод отсортированного массива.
        for user in sorted_user_list[::-1]:
            print(user[2])