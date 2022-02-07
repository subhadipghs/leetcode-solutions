import unittest


class Node:
    """
        Implementation of a node in hte linked list
    """

    def __init__(self, val: int, next=None) -> None:
        self.val = val
        self.next = next

    def get_value(self) -> int:
        return self.val


class List:
    """
        Implementation of singly linked list
    """

    def __init__(self) -> None:
        self.head = None
        self.count = 0

    def insert_at_begin(self, val: int) -> bool:
        """
            Insert a node at the beginning of the list
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.count += 1
        return True

    def append(self, val: int) -> bool:
        """
            Insert at the end of the list
            0. head -> None
            1. append 10 => head -> [10] -> None
            2. append 20 -> head -> [10 ] -> [20] -> None 
        """
        new_node = Node(val)
        ptr = self.head
        # if the list is empty then just add the node to head
        if ptr == None:
            self.count += 1
            self.head = new_node
            return True
        # if not ptr is not empty then just add iterate through the nodes and find where the
        while ptr.next != None:
            ptr = ptr.next
        self.count += 1
        ptr.next = new_node
        new_node.next = None
        return True

    def size(self) -> int:
        return self.count

    def get_list(self):
        l = []
        ptr = self.head
        while ptr != None:
            l.append(ptr.val)
            ptr = ptr.next
        return l

    def print(self) -> None:
        ptr = self.head
        while ptr != None:
            print(ptr.val)
            ptr = ptr.next


class TestsSum(unittest.TestCase):
    def test_correct_size(self):
        l = List()
        for i in [1, 2, 3, 4]:
            l.append(i)
        self.assertEqual(l.size(), 4)

    def test_size_zero(self):
        l = List()
        self.assertEqual(l.size(), 0)


if __name__ == "__main__":
    unittest.main()
