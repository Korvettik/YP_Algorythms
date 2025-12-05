def sift_up(heap, idx) -> int:
    # базовый случай для рекурсии
    if idx == 1:  #  в куче всего [None, текущий добавленный], т.е. всего 1 элемент. Его не с чем сравнивать и перемещать.
        return idx

    parent_index = idx // 2  # по формуле находим индекс родительского элемента

    if heap[idx] > heap[parent_index]:
        heap[idx], heap[parent_index] = heap[parent_index], heap[idx]  # меняем местами, чтобы значение родителя было больше значения ребенка
        sift_up(heap, parent_index)





def test():
    sample = [-1, 12, 6, 8, 3, 15, 7]
    assert sift_up(sample, 5) == 1

if __name__ == '__main__':
    test()