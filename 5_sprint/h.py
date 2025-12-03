import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> int:
    all_tracks = []

    def check_node(all_tracks, concatination_track, node):

        if node is None:
            return
        else:
            concatination_track += str(node.value)  # конкатинируем путь

        if node.left is None and node.right is None:
            all_tracks.append(concatination_track)
            return
        else:
            check_node(all_tracks, concatination_track, node.left)
            check_node(all_tracks, concatination_track, node.right)
        return

    check_node(all_tracks, '', root)
    #print(all_tracks, sum(map(int, all_tracks)))
    return sum(map(int, all_tracks))



def test():
    node1 = Node(2, None, None)
    node2 = Node(1, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(2, None, None)
    node5 = Node(1, node4, node3)

    assert solution(node5) == 275


if __name__ == '__main__':
    test()