import typing_extensions
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

    def remove_node(self, val: int) -> bool:
        """
            Remove node with provided value
        """
        r = self.head
        parent_node = self.head
        flag = False
        while r.next != None:
            if r.val == val:
                flag = True
                break
            parent_node = r
            r = r.next
        # now we have the parent node
        if flag:
            parent_node.next = r.next
            del r
            self.count -= 1
        return flag

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

    def make_list(self) -> list:
        l = []
        ref = self.head
        while ref != None:
            l.append(ref.val)
            ref = ref.next
        return l

    def __eq__(self, __o: object) -> bool:
        ref = self.head
        other_ref = __o.head
        print(__o.size())
        if self.size() != __o.size():
            return False
        while ref != None and other_ref != None:
            if ref.val != other_ref.val:
                return False
            ref = ref.next
            other_ref = other_ref.next
        return True

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
            print(ptr.val, end=" ")
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

    def test_remove_node_from_middle(self):
        l = List()
        """
            [1, 2, 3, 4, 5]
        """
        for i in [1, 2, 4, 5, 8]:
            l.append(i)
        self.assertEqual(l.size(), 5)
        l.remove_node(4)
        self.assertEqual(l.size(), 4)
        self.assertEqual(l.make_list(), [1, 2, 5, 8])

    def test_remove_node_from_head(self):
        l = List()
        """
            [1, 2, 3, 4, 5]
        """
        for i in [1, 2, 4, 5, 8]:
            l.append(i)
        self.assertEqual(l.size(), 5)
        l.remove_node(1)
        self.assertEqual(l.size(), 4)
        self.assertEqual(l.make_list(), [2, 4, 5, 8])

    def test_equality(self):
        l = [1, 2, 4, 5]
        c1 = List()
        c2 = List()
        for i in l:
            c1.append(i)
            c2.append(i)
        self.assertTrue(c1 == c2)


if __name__ == "__main__":
    unittest.main()
