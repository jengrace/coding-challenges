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


class Tree:
    def __init__(self):
        self.max_so_far = 0
        self.max_node = None
        self.root = None

    def get_deepest_node(self, current, level=0):
        if current.lchild is not None:
            self.get_deepest_node(current.lchild, level=level+1)
        if current.rchild is not None:
            self.get_deepest_node(current.rchild, level=level+1)
        if level >= self.max_so_far:
            self.max_so_far = level
            self.max_node = current
        return self.max_node.data


def test():

    t1 = Tree()
    t1.root = Node(9)
    t1.root.lchild = Node(4)
    t1.root.rchild = Node(15)
    t1.root.rchild.lchild = Node(12)
    t1.root.rchild.rchild = Node(17)
    t1.root.lchild.lchild = Node(2)
    t1.root.lchild.rchild = Node(6)
    t1.root.lchild.rchild.rchild = Node(10)
    assert t1.get_deepest_node(t1.root) == 10

    t2 = Tree()
    t2.root = Node(10)
    t2.root.lchild = Node(5)
    t2.root.lchild.lchild = Node(4)
    t2.root.lchild.rchild = Node(6)
    t2.root.lchild.lchild.lchild = Node(3)
    t2.root.lchild.lchild.lchild.lchild = Node(2)
    t2.root.rchild = Node(11)
    t2.root.rchild.rchild = Node(12)
    assert t2.get_deepest_node(t2.root) == 2

    t3 = Tree()
    t3.root = Node(5)
    assert t3.get_deepest_node(t3.root) == 5

    t4 = Tree()
    t4.root = Node(10)
    t4.root.lchild = Node(5)
    assert t4.get_deepest_node(t4.root) == 5
    t4.root.lchild.lchild = Node(3)
    assert t4.get_deepest_node(t4.root) == 3

    print 'Tests passed'

test()
