
import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class DoubleConnectedNode:
        def __init__(self, value, next=None, prev=None):
            self.value = value
            self.next = next
            self.prev = prev


def solution(node):
    """функция точки входа"""
    # новый лимит (по задачке) увеличивать не требуется

    class Data:
        def __init__(self):
            self.new_head_node = None  # возвращаемая новая голова
            self.node_next = None # текущий проходимый узел

    data = Data()
    data.new_head_node = node  # запоминаем текущую голову

    recursion_logic(node, data)

    print(f'new_head_node {data.new_head_node.value}')
    return data.new_head_node



def recursion_logic(node, data):

    # записали следующий от текущего
    data.node_next = node.next

    # меняем местами локально на элементе
    next = node.next
    prev = node.prev

    node.next = prev
    node.prev = next

    print(node.value)
    if data.node_next:
        recursion_logic(data.node_next, data)
    else:
        data.new_head_node = node  # прописали последний










def test():
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    # node0.next = node1
    #
    # node1.prev = node0
    # node1.next = node2
    #
    # node2.prev = node1
    # node2.next = node3
    #
    # node3.prev = node2

    new_head = solution(node0)

    # assert new_head is node3
    # assert node3.next is node2
    # assert node2.next is node1
    # assert node2.prev is node3
    # assert node1.next is node0
    # assert node1.prev is node2
    # assert node0.prev is node1

    def test_recursion_items(node):
        """функция основной логики"""
        print(node.value)
        if node.next_item:
            test_recursion_items(node.next_item)

    test_recursion_items(node3)

if __name__ == '__main__':
    test()
