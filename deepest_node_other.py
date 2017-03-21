# Problem: Find deepest child node
#           9
#         /  \
#       4     ----15
#     /  \        /  \
#   2      6    12      17
#           \
#             10


class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

node1 = Node(9)
node1.lchild = Node(4)
node1.rchild = Node(15)
node1.rchild.lchild = Node(12)
node1.rchild.rchild = Node(17)
node1.lchild.lchild = Node(2)
node1.lchild.rchild = Node(6)
node1.lchild.rchild.rchild = Node(10)


def get_deepest_node(current_node, level=0):
    left = None
    right = None
    if current_node.lchild is not None:
        left = get_deepest_node(current_node.lchild, level=level+1)
    if current_node.rchild is not None:
        right = get_deepest_node(current_node.rchild, level=level+1)
    if left is not None and right is not None:
        if left[1] > right[1]:
            return (left[0], left[1])
        else:
            return (right[0], right[1])
    elif left is not None:
        return (left[0], left[1])
    elif right is not None:
        return (right[0], right[1])
    return (current_node, level)

print get_deepest_node(node1)[0].data
