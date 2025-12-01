import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> bool:

    counter_flag = 0

    stack = [root]   # хранилище текущего или пары узлов

    # итеративный подход --- дергаем все-все элементы в список для анализов
    while stack:
        node = stack.pop()   # вырезали, схватили

        # если у него были дети --- кладем их в хранилище, для цикличного анализа
        if node.right:
            stack.append(node.right)
            counter_flag += 1
        if node.left:
            stack.append(node.left)
            counter_flag -= 1

    if counter_flag == 0:
        return  True
    else:
        return  False






def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


if __name__ == '__main__':
    test()