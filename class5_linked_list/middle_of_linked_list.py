class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = fast = head

        while fast != None and fast.next != None:

            slow = slow.next
            fast = fast.next.next

        
        return slow
