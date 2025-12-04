import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if not LOCAL:
    from node import Node

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value


def insert(root, key):

    def check_node(node, parent, key):

        if node is None:
            if key >= parent.value:
                new_node = Node(value=key)
                parent.right = new_node
            else:
                new_node = Node(value=key)
                parent.left = new_node
            return

        if key >= node.value:
            check_node(node.right, node, key)  # по правой ветке пошли
        else:
            check_node(node.left, node, key)  # по левой ветке пошли

    check_node(root, root, key)

    return root


def test():
    node1 = Node(None, None, 7)
    node2 = Node(node1, None, 8)
    node3 = Node(None, node2, 7)
    new_head = insert(node3, 6)
    assert new_head is node3
    assert new_head.left.value == 6


if __name__ == '__main__':
    test()