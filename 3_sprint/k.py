def merge(arr, lf, mid, rg):
    # Создаем временные массивы для левой и правой частей
    left_part = arr[lf:mid]
    right_part = arr[mid:rg]

    i = j = 0  # Индексы для left_part и right_part
    k = lf  # Индекс для основного массива

    # Сливаем временные массивы обратно в array[left..right]
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    # Копируем оставшиеся элементы left_part, если есть
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    # Копируем оставшиеся элементы right_part, если есть
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

    return arr




def merge_sort(arr, lf, rg):
    # Базовый случай: если в подмассиве 1 элемент или меньше, он уже отсортирован
    if rg - lf <= 1:
        return

    # Находим середину
    mid = (lf + rg) // 2

    # Рекурсивно сортируем левую и правую части
    merge_sort(arr, lf, mid)
    merge_sort(arr, mid, rg)

    # Сливаем отсортированные части
    merge(arr, lf, mid, rg)



def test():
	a = [1, 4, 9, 2, 10, 11]
	b = merge(a, 0, 3, 6)
	expected = [1, 2, 4, 9, 10, 11]
	assert b == expected

	c = [1, 4, 2, 10, 1, 2]
	merge_sort(c, 0 , 6)
	expected = [1, 1, 2, 2, 4, 10]
	assert c == expected

if __name__ == '__main__':
    test()