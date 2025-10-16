import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item



def solution(node, idx):
    """функция точки входа"""
    import sys
    sys.setrecursionlimit(5000)  # новый лимит (по задачке)

    class Data:
        def __init__(self):
            self.new_head_node = None  # возвращаемая новая голова
            self.counter = 0  # счетчик глубины связного списка
            self.node_previous = None  # ссылка на предыдущий узел

    data = Data()
    data.new_head_node = node  # запоминаем текущую голову

    recursion_logic(node, idx, data)
    #print(f'result {data.new_head_node.value}')
    return data.new_head_node



def recursion_logic(node, idx, data):

    node_next = node.next_item

    if idx == data.counter:
        if idx == 0:  # если нужно удалить саму голову
            data.new_head_node = node_next  # просто новая голова
            return data
        else:
            # вырезали текущий = соединили предыдущий со следующим от вырезанного
            # даже если там пустота
            data.node_previous.next_item = node.next_item
            return data

    else:
        data.counter += 1
        data.node_previous = node  # запоминаем предыдущий узел
        recursion_logic(node_next, idx, data) # идем в следующий узел








def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)

    new_head = solution(node0, 0)

    # assert new_head is node0
    # assert new_head.next_item is node2
    # assert new_head.next_item.next_item is node3
    # assert new_head.next_item.next_item.next_item is None

    # result is node0 -> node2 -> node3


    def test_recursion_items(node):
        """функция основной логики"""
        print(node.value)
        if node.next_item:
            test_recursion_items(node.next_item)

    test_recursion_items(new_head)




if __name__ == '__main__':
    test()