from typing import Optional
import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value
else:
    from node import Node



# """
#          5
#    /          \
#   1           10
#   /\         /  \
#     3       8
#     /\      /\
#    2       6
#   /\      /\
#
# """



def remove(root, key):

    # Если дерево пустое / конец дерева / узла не нашли
    if root == None:
        return None

    # Ищем узел для удаления (не факт что дерево отсортировано)
    # Руководствуемся правилом:
    # 1) что ищется текущий корень (нода).
    # 2) элементы больше ноды по правому ребру, меньше ноды - по левому ребру

    if key < root.value:
        root.left = remove(root.left, key)  # рекурсия. пошли искать по левому ребру.
        # Т.е. перезаписываем левое поддерево, т.к. внутри него могут быть изменения
    elif key > root.value:
        root.right = remove(root.right, key)


    else:
        # Нашли узел для удаления (т.е. текущий узел либо тот что ищем, либо его нет - значит ничего не делаем)
        # Удалить искомый элемент - значит нужно откорректировать дерево, т.е. соединить ребра родительского и дочернего так,
        # чтобы удаляемый элемент утратил связь с деревом

        # 1 -- ВАРИАНТ, если из детей кто-то один (левый или правый)--
        if root.left == None:
            return root.right  # заменяем текущий узел на правого ребенка (даже если там None)
            # - рекурсия тут нас возвращает в предыдущую итерацию присваивания root.left = или root.right =
        elif root.right == None:
            return root.left

        # 2 -- ВАРИАНТ, если нет детей --
        # в данном случае, если узел, куда переводится ребро также равен None,
        # то и вернется в предыдущую итерацию присваивания root.left = или root.right = также None

        # 3 -- ВАРИАНТ, если у узла два ребенка
        # Чтобы соблюсти правило дерева (когда по правому ребру элемент больший,
        # а по левому меньший относительно самого узла), нужно выбрать по всем правым ребрам узлов такое,
        # чтобы значение его было минимально в этом поддереве.
        # 1) Все узлы в правом поддереве больше удаляемого узла - новый правый ребенок будет больше родителя
        # 2) Минимальный узел в правом поддереве гарантированно больше всех узлов в левом поддереве удаляемого узла
        # 3) + он меньше всех остальных узлов в правом поддереве

        # Находим минимальный узел в правом поддереве
        min_node = finding_minimum_node(root.right)

        # Заменяем значение текущего узла на значение минимального
        root.value = min_node.value

        # Удаляем минимальный узел из правого поддерева
        root.right = remove(root.right, min_node.value)

    return root  # возвращаем текущую голову измененного (где-то внутри) дерева


def finding_minimum_node(node):
    """Ищем узел с минимальным значением в поддереве"""
    current_node = node
    while current_node.left != None:
        current_node = current_node.left
    return current_node







def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)

    # new_head = remove(node1, 2)
    # assert new_head.value == 2

    new_head = remove(node7, 10)
    print(f'head {new_head.value}')
    assert new_head.value == 5
    print(f'right {new_head.right.value}')
    assert new_head.right is node5
    assert new_head.right.value == 8


if __name__ == '__main__':
    test()