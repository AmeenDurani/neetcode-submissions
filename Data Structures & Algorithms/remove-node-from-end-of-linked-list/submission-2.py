# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse.
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        rev = prev

        # count.
        nxt, curr, prev = prev, None, None
        for i in range(n):
            prev = curr
            curr = nxt
            nxt = nxt.next
        
        # remove.
        if prev:
            prev.next = nxt
        else:
            rev = nxt
        
        # reverse.
        prev, curr = None, rev
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

