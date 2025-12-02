import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> int:
    if not root:
        return 0

    # Используем список, чтобы изменять значение внутри рекурсии
    result = [float('-inf')]   # список есть изменяемый объект, поэтому в функции мы его видим.
    # Если просто переменная, то питуон думает что мы создаем или переприсваиваем его,
    # а значит это только внутри функции

    def dfs(node):
        if not node:
            return 0  # в эту вершину не идем

        # вычисляем возможные максимумы по каждому ребенку.

        # рекурсивно по левой ветке берем максимальное значение
        left = max(dfs(node.left), 0)  # Если отрицательно - не берем
        # рекурсивно по правой ветке берем максимальное значение
        right = max(dfs(node.right), 0)

        # Обновляем глобальный результат (сравниваем то, что уже есть с вариативной цепочкой через одну арку (текущая верщина + ее левый максимум + ее правый максимум))
        result[0] = max(result[0], node.value + left + right)

        # Возвращаем лучший путь для родителя (вершины арки)
        return node.value + max(left, right)

    dfs(root)
    return result[0]



def test():
    node1 = Node(5, None, None)
    node2 = Node(1, None, None)
    node3 = Node(-3, node2, node1)
    node4 = Node(2, None, None)
    node5 = Node(2, node4, node3)
    assert solution(node5) == 6


if __name__ == '__main__':
    test()