# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count =1
        a = head
        b = head
        while a.next is not None:
            a = a.next
            count = count + 1
        n = math.ceil((count+1)/2)
        for i in range(1,n):
            b = b.next
        return b
            
        

        
