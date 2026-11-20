# Definition for singly-linked list.
from locale import currency
from traceback import print_tb


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        nums = []

        current = head

        while(current != None):
            nums.append(current.val)
            current = current.next


        i = len(nums) - 1

        current = head

        while i >= 0:
            current.val = nums[i]
            current = current.next
            i -= 1

        return head



n = [2,3,4,5]

head = ListNode(1, None)
for num in n:
    curre

s = Solution()
