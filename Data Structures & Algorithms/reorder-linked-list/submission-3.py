# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle of the list.
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # split into two lists.
        first = head
        second = slow.next
        slow.next = None

        # reverse the second half.
        prev = None
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next
        second = prev
        
        # merge the two.
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
    