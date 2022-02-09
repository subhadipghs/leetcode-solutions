# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
from re import L
from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c = 0
        r = self.head
        flag = False
        while r != None:
            c += 1
            r = r.next
        print(c)
        r = self.head
        parent_node = self.head
        current = 0
        while r.next != None:
            if current == c - 1:
                flag = True
                break
            parent_node = r
            r = r.next
        # now we have the parent node
        if flag:
            parent_node.next = r.next
            del r
        return flag


def test_remove_nth_node():

    l = ListNode(1)

    for v in [2, 3, 4]:
        ref = l
        while ref.next != None:
            ref = ref.next
        ref.next = ListNode(v)

    result = Solution().removeNthFromEnd(l, 2)
    out(result)


def make(l: list):

    for v in l:
        ref = l
        while ref.next != None:
            ref = ref.next
        ref.next = ListNode(v)


def get_arr(l: ListNode):
    r = l
    rt = []
    while r != None:
        rt.append(r.val)
        r = r.next
    return rt


def out(l):
    ref = l
    while ref != None:
        print(ref.val, end=' ')
        ref = ref.next


if __name__ == '__main__':
    test_remove_nth_node()
