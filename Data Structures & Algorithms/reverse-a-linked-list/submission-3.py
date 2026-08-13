# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l, c = None, head

        while c != None:
            r = c.next
            c.next = l
            l = c
            c = r
            r = r.next if r is not None else None
            
        return l

        