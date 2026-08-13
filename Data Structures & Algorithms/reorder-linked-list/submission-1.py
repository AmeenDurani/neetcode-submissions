# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # make a copy of the reverse order
        prev, rev, count, cpy = None, None, 0, head
        while head:
            rev = ListNode(head.val, prev)
            prev = rev
            head= head.next
            count += 1
        head = cpy
        i = count // 2

        # traverse the original, appending the reverse index
        prev = None
        while head and i > 0: 
            temp = head.next
            head.next = rev
            prev = head.next
            rev = rev.next
            head.next.next = temp
            head = temp
            i -= 1
        if count % 2 == 1: head.next = None
        else: prev.next = None
        head = cpy