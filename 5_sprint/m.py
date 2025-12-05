def sift_up(heap, idx) -> int:
    while idx > 1:
        parent = idx // 2
        if heap[idx] > heap[parent]:
            # Меняем местами с родителем
            heap[idx], heap[parent] = heap[parent], heap[idx]
            idx = parent
        else:
            break
    return idx



def test():
    sample = [-1, 12, 6, 8, 3, 15, 7]
    assert sift_up(sample, 5) == 1

if __name__ == '__main__':
    test()