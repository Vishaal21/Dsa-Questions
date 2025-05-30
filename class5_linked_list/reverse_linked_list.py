class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        while curr != None:

            nbr = curr.next
            curr.next = prev

            prev = curr
            curr = nbr

        
        return prev