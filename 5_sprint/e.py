import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left





def solution(root) -> bool:

    def check_node(node, min_val, max_val):
        # Пустое поддерево тоже подойдет
        if node is None:
            return True

        # Текущее значение должно быть строго в пределах (min_val - для правого, max_val - для левого)
        if node.value <= min_val or node.value >= max_val:
            return False

        # Проверяем левое и правое поддеревья
        # Для левого: максимальное значение становится текущим значением
        # Для правого: минимальное значение становится текущим значением

        # рекурсивно проверяем левый и правый элементы
        return (check_node(node.left, min_val, node.value)  # для левого, max_val это значение корня
                and check_node(node.right, node.value, max_val))  # для правого, min_val это значение корня

    # Изначально вызываем с бесконечными границами
    return check_node(root, float('-inf'), float('inf'))  # эти бесконечности будут тянуться до самого дна



def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)

if __name__ == '__main__':
    test()