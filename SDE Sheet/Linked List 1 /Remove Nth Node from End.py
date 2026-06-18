# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a = head
        b = head.next
        c = head
        prev = head
        count = 1
        while a.next is not None:
            count = count + 1
            a = a.next
        if count == n:
            head = c.next
            c.next = None
            return head

        for i in range(1,count-n):
            b = b.next
            prev = prev.next
        prev.next = b.next
        b.next =None
        return c
                
        
