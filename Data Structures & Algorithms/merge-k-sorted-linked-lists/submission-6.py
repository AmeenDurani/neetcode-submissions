# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap, faux = [], ListNode()
        head = faux

        for k, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, k, node))

        while heap:
            _, k, node = heapq.heappop(heap)
            head.next = node
            node = node.next
            head = head.next
            if node:
                heapq.heappush(heap, (node.val, k, node))

        return faux.next
