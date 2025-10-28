#

# -- ПРИНЦИП РАБОТЫ ---

# -- ДОКАЗАТЕЛЬСТВА КОРРЕКТНОСТИ --

# -- ОПРЕДЕЛЕНИЕ СЛОЖНОСТИ АЛГОРИТМА --


def broken_search(nums, target) -> int:
    """вернуть индекс элемента, равного k, если такой есть в массиве (нумерация с нуля). Если элемент не найден, функция должна вернуть −1

    сдвинула данные исходной отсортированной последовательности (при этом массив все равно мог остаться отсортированным"""

    # бинарный поиск работает только на отсортированной последовательности

    # чтобы всегда хранить индексы границ
    index_left = 0  # левая граница
    index_right = len(nums)  # правая граница

    while index_left < index_right:  # чтобы не рекурсию использовать, а цикл + это условие выхода (индексы не сравнялись, т.е. что-то в диапазоне есть)
        # промежуток не пуст
        index_middle = (index_left + index_right) // 2  # значение индекса, что расположен примерно в середине рассматриваемого индекс-списка
        print(f'index_middle {index_middle}')
        print(f'левая часть {nums[index_left:index_middle+1]}, правая часть {nums[index_middle+1:index_right]}')

        if nums[index_middle] == target:  # нашли
            print(index_middle)
            return index_middle

        elif nums[index_middle] < target: # искомый элемент следует искать в левой половине
            index_right = index_middle

        else:  # иначе следует искать в правой половине
            index_left = index_middle + 1


    print(-1)
    return -1 # Значение не найдено, промежуток пуст




def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6




# left, right = 0, len(arr) - 1 # Индексы левой и правой границы
#
# while left <= right:
#     mid = (left + right) // 2
#     if arr[mid] == value:
#         return mid
#     elif arr[mid] < value:
#         left = mid + 1
#     else:
#         right = mid - 1
#
# return -1 # Значение не найдено


# def broken_search(arr, x, left, right):
#     if right <= left: # промежуток пуст
#         return -1
#     # промежуток не пуст
#     mid = (left + right) // 2
#     if arr[mid] == x:  # центральный элемент — искомый
#         return mid
#     elif x < arr[mid]: # искомый элемент меньше центрального значит следует искать в левой половине
#         return broken_search(arr, x, left, mid)
#     else: # иначе следует искать в правой половине
#         return broken_search(arr, x, mid + 1, right)


 # if (
 #            nums[mid] <= nums[left] <= target
 #            or target <= nums[mid] <= nums[left]
 #            or nums[left] <= target <= nums[mid]
 #        ):



# n = int(input().strip())  # длина массива
# k = int(input().strip())  # искомый элемент
# array = list(map(int, input().strip().split()))  # целые числа, сам массив

# print(n, k, array)


test()

