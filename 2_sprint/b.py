import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node):
    """функция точки входа"""
    import sys
    #print(sys.getrecursionlimit())  # Выводим существующий лимит рекурсии
    sys.setrecursionlimit(5000)  # новый лимит (по задачке)

    recursion_items(node)

def recursion_items(node):
    """функция основной логики"""
    print(node.value)
    if node.next_item:
        recursion_items(node.next_item)




def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    solution(node0)
    # Output is:
    # node0
    # node1
    # node2
    # node3


if __name__ == '__main__':
    test()