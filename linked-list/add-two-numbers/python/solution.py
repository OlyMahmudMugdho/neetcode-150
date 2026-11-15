# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        num1 = 0
        num2 = 0

        mul1 = 1

        while(l1):
            num1 += (mul1 * l1.val)
            mul1 *= 10
            l1 = l1.next

        mul2 = 1

        while(l2):
            num2 += (mul2 * l2.val)
            mul2 *= 10
            l2 = l2.next

        sum = num1 + num2

        if sum == 0:
            return ListNode(0)

        result = []

        while sum != 0:
            digit = sum % 10
            result.append(digit)
            sum = sum // 10


        sumList = ListNode(-1)
        temp = sumList

        for num in result:
            sumList.next = ListNode(num)
            sumList = sumList.next

        return temp.next