# Remove Nth Node From End of List
# Problem Number - 19
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create a dummy node pointing to head
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy

        # move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # move both pointers until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next

        # remove the nth node from the end
        slow.next = slow.next.next

        return dummy.next
