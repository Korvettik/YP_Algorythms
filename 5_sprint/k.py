import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value


def print_range(node, l, r):
    nodes_collection = []

    def check_node(node, l, r):

        if node is None:
            return

        if l <= node.value <= r:
            nodes_collection.append(node.value)


        check_node(node.left, l, r)
        check_node(node.right, l, r)

    check_node(node, l, r)
    collection = sorted(nodes_collection)
    print(*collection, sep='\n')


def test():
    node1 = Node(None, None, 2)
    node2 = Node(None, node1, 1)
    node3 = Node(None, None, 8)
    node4 = Node(None, node3, 8)
    node5 = Node(node4, None, 9)
    node6 = Node(node5, None, 10)
    node7 = Node(node2, node6, 5)
    print_range(node7, 2, 8)
    # expected output: 2 5 8 8


if __name__ == '__main__':
    test()