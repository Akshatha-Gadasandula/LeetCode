# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        a = l1
        b = l2
        carry = 0
        c = ListNode(0)
        head = c
        while a is not None or b is not None or carry:
            x = a.val if a is not None else 0
            y = b.val if b is not None else 0
            
            total = x + y + carry

            carry = total // 10
            digit = total % 10
            
            c.next = ListNode(digit)
            c = c.next

            if a is not None :
                a = a.next

            if b is not None :
                b = b.next
        return head.next



        
        
