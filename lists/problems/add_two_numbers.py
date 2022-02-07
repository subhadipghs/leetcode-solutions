# Leetcode Question Link: https://leetcode.com/problems/add-two-numbers/
from typing import Optional


class ListNode:
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
        new_node = ListNode(val)
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
        new_node = ListNode(val)
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
            print(ptr.val, end=" ")
            ptr = ptr.next
        print('\n')


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        v1 = 0  # sum is zero
        v2 = 0
        sum = 0
        ptr = l1
        # first number
        counter = 0
        while ptr != None:
            v1 += ptr.val*(10**counter)
            ptr = ptr.next
            counter += 1
        # second number
        ptr = l2
        counter = 0
        while ptr != None:
            v2 += ptr.val*(10**counter)
            ptr = ptr.next
            counter += 1
        # sum of the two numbers
        sum = v1 + v2
        l = None
        if sum == 0:
            return ListNode(0)
        else:
            while sum != 0:
                digit = sum % 10
                sum = sum // 10
                new_node = ListNode(digit)
                # append to the list
                ref = l
                # if the list is empty then just add the node to head
                if ref == None:
                    l = new_node
                else:
                    # if not ref is not empty then just add iterate through the nodes and find where the
                    while ref.next != None:
                        ref = ref.next
                    ref.next = new_node
                    new_node.next = None
        return l

    def optimized_add_two_sum(self, l1, l2):
        ptr1 = l1
        ptr2 = l2
        merged = ListNode(0)
        carry = 0
        while ptr1 or ptr2 or carry:
            val1 = ptr1.val if ptr1 else 0
            val2 = ptr2.val if ptr2 else 0
            sum = val1 + val2 + carry
            digit = sum if sum < 10 else (sum - 10)
            ref = merged
            while ref.next != None:
                ref = ref.next
            ref.next = ListNode(digit)
            carry = 1 if sum >= 10 else 0
            ptr1 = ptr1.next if ptr1 else None
            ptr2 = ptr2.next if ptr2 else None
        return merged.next


def out(l) -> None:
    ptr = l
    while ptr != None:
        print(ptr.val, end=" ")
        ptr = ptr.next


def test_add_two_numbers():
    l1 = List()
    l2 = List()
    for i in [2, 4, 6]:
        l1.append(i)
    for i in [5, 6, 4, 9]:
        l2.append(i)
    m = Solution().optimized_add_two_sum(l1.head, l2.head)
    out(m)


if __name__ == '__main__':
    test_add_two_numbers()
