def sift_down(heap, idx) -> int:
    n = len(heap) - 1  # индекс последнего элемента в куче
    left = 2 * idx  # индекс левого ребенка
    right = 2 * idx + 1  # индекс правого ребенка
    largest = idx  # представим, что индекс самого большого элемента в арке-пирамиде это тот, что дали

    # Находим индекс максимального элемента среди текущего и его потомков
    if left <= n and heap[left] > heap[largest]:
        largest = left
    if right <= n and heap[right] > heap[largest]:
        largest = right

    # Если текущий элемент не максимальный, меняем местами и продолжаем просеивание
    if largest != idx:
        heap[idx], heap[largest] = heap[largest], heap[idx]
        return sift_down(heap, largest)

    return idx


def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5



if __name__ == '__main__':
    test()