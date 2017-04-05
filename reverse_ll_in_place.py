class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    """Linked list."""

    def __init__(self, head=None):
        self.head = head

    def as_string(self):
        """Represent data for this list as a string.

        >>> LinkedList(Node(3)).as_string()
        '3'

        >>> LinkedList(Node(3, Node(2, Node(1)))).as_string()
        '321'
        """

        out = []
        n = self.head

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(out)


def reverse_linked_list_in_place(lst):
    """Given linked list, reverse the nodes in this linked list in place."""

    prev = None
    current = lst.head

    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    lst.head = prev

ll = LinkedList(Node(1, Node(2, Node(3))))
reverse_linked_list_in_place(ll)
print ll.as_string()
