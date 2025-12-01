import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> bool:

    def get_height(node):
        """Возвращает высоту поддерева, если оно сбалансировано, иначе -1"""
        if node is None:
            return 0

        left_height = get_height(node.left)
        if left_height == -1:
            return -1

        right_height = get_height(node.right)
        if right_height == -1:
            return -1

        # Проверяем балансировку текущего узла
        if abs(left_height - right_height) > 1:
            return -1

        # Возвращаем высоту текущего поддерева
        return 1 + max(left_height, right_height)

    return get_height(root) != -1











def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


if __name__ == '__main__':
    test()