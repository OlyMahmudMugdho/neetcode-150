class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if head == None:
            return

        lastNode = head
        length = 0

        while(lastNode):
            lastNode = lastNode.next
            length += 1


        if length == 1 and n == 1:
            return None
        

        toRemove = length - n

        if toRemove == 0:
            head = head.next
            return head

        temp = head
        i = 0

        while(i < toRemove-1):
            temp = temp.next
            i += 1

        if length == n:
            temp.next = None
            return head

        temp.next = temp.next.next

        return head
