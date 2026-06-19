# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a = list1
        b = list2
        c = ListNode(0)
        head = c
        while a and b:
            x = a.val if a is not None else 0
                # x = a.val
            y = b.val if b is not None else 0
                # y = b.val
            if x <y:
                add_node = ListNode(x)
                c.next = add_node
                c = c.next
                if a is not None:
                    a = a.next 
            elif x == y:
                add_node = ListNode(x)
                c.next = add_node
                c = c.next
                if a is not None:
                    a = a.next 
                add_node = ListNode(y)
                c.next = add_node
                c = c.next
                if b is not None:
                    b = b.next

            else :
                add_node = ListNode(y)
                c.next = add_node
                c = c.next
                if b is not None:
                    b = b.next
        while a :
            x = a.val
            add_node = ListNode(x)
            c.next = add_node
            c = c.next
            if a is not None:
                a = a.next
        while b :
            y = b.val
            add_node = ListNode(y)
            c.next = add_node
            c = c.next
            if b is not None:
                b = b.next

        return head.next
            
        
