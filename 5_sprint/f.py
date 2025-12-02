import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left

def solution(root) -> int:

    max_track = []

    def check_node(max_track, step_count, node):
        if node is None:
            max_track.append(step_count)
            return
        else:
            step_count += 1
            check_node(max_track, step_count, node.left)
            check_node(max_track, step_count, node.right)


        return max(max_track)

    res = check_node(max_track, 0, root)
    #print(res)
    return res




def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5) == 3

if __name__ == '__main__':
    test()