#

# -- ПРИНЦИП РАБОТЫ ---

# -- ДОКАЗАТЕЛЬСТВА КОРРЕКТНОСТИ --

# -- ОПРЕДЕЛЕНИЕ СЛОЖНОСТИ АЛГОРИТМА --


def broken_search(nums, target) -> int:
    """вернуть индекс элемента, равного k, если такой есть в массиве (нумерация с нуля). Если элемент не найден, функция должна вернуть −1"""

    # бинарный поиск

    return


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6






n = int(input().strip())  # длина массива
k = int(input().strip())  # искомый элемент
array = list(map(int, input().strip().split()))  # целые числа, сам массив

print(n, k, array)
# broken_search(array, k)

