import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left



def solution(root) -> int:
    if root is None:
        return float('-inf')

    stack = [root]   # хранилище текущего или пары узлов
    max_val = float('-inf')   # бесконечное отрицательное число --- самое маленькое

    # итеративный подход --- дергаем все-все элементы в список для анализов
    while stack:
        node = stack.pop()   # вырезали, схватили
        max_val = max(max_val, node.value)  # отобрали, если больше

        # если у него были дети --- кладем их в хранилище, для цикличного анализа
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return max_val








def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3


if __name__ == '__main__':
    test()