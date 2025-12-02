import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left



def is_twins(root1, root2):

    # Если оба пустые, а значит одинаковые, т.е. существует только один общий корень
    if root1 is None and root2 is None:
        return True
    # если есть только один ребенок у общей головы
    if root1 is None or root2 is None:
        return False

    # дошли до этого момента (обратным ходом рекрсии здесь будет цепочка True True ...)
    return (root1.value == root2.value    # если значения корней равны
            and is_twins(root1.left, root2.left)  # рекурсивно сравниваем левую голову левого ребенка и левую голову правого ребенка
            and is_twins(root1.right, root2.right))  # рекурсивно сравниваем правую голову левого ребенка и правую голову правого ребенка




def solution(root1, root2) -> bool:
    return is_twins(root1, root2)


def test():
    node1 = Node(1, None, None)
    node2 = Node(2, None, None)
    node3 = Node(3, node1, node2)

    node4 = Node(1, None, None)
    node5 = Node(2, None, None)
    node6 = Node(3, node4, node5)

    assert solution(node3, node6)


if __name__ == '__main__':
    test()