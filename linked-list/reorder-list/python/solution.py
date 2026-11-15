# Definition for singly-linked list.
from pyparsing import nums
from urllib3 import Retry


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        num_arrays = []
        current = head

        while(current):
            num_arrays.append(current.val)
            current = current.next

        n = len(num_arrays)
        p1 = 0
        p2 = n - 1


        temp = head

        while (p1 <= p2):
            temp.val = num_arrays[p1]
            temp = temp.next
            if not temp:
                return
            temp.val = num_arrays[p2]
            temp = temp.next
            if not temp:
                return

            p1 += 1
            p2 -= 1