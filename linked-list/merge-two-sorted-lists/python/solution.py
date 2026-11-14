# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        nums = []

        left = list1
        right = list2

        while((left != None) and (right != None)):
            if (left.val < right.val):
                nums.append(left.val)
                left = left.next

            else:
                nums.append(right.val)
                right = right.next

        while(left != None):
            nums.append(left.val)
            left = left.next

        while(right != None):
            nums.append(right.val)
            right = right.next


        if len(nums) == 0:
            return None

        result = ListNode(nums[0], None)
        current = result

        i = 1

        while(i < len(nums)):
            current.next = ListNode(nums[i], None)
            current = current.next
            i += 1


        return result