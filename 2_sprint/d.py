import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item





def solution(node, elem):
    """функция точки входа"""
    import sys
    sys.setrecursionlimit(10000)  # новый лимит (по задачке)

    class Data:
        def __init__(self):
            self.index = None  # возвращаемый индекс глубины
            self.counter = 0  # счетчик глубины связного списка


    data = Data()

    recursion_logic(data, node, elem)

    if data.index is not None:
        return data.index
    else:
        return -1


def recursion_logic(data, node, elem):
    """функция основной логики"""
    #print(node.value)

    if node.value == elem:
        data.index = data.counter
        return
    else:
        data.counter += 1

        if node.next_item:
            recursion_logic(data, node.next_item, elem)









def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)

    idx = solution(node2, "node3")

    #assert idx == 2
    print(idx)





if __name__ == '__main__':
    test()