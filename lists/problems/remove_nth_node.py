# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
from typing import Optional
from unittest import TestCase
import unittest

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


class TestRemoveNthNode(TestCase):
    def test_remove_nth_node(self):
        l = make([1, 2, 3, 4])


def make(l: list):
    fn = ListNode(l[0])
    for v in range(1, len(l)):
        ref = fn
        while ref.next != None:
            ref = ref.next
        ref.next = ListNode(l[v])
    return fn


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
    unittest.main()
