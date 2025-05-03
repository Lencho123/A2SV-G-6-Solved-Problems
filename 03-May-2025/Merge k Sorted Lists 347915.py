# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, lst in enumerate(lists):
            if lst:
                heappush(heap,(lst.val, i, lst))
        
        head = ListNode()
        cur = head

        while heap:
            val,i,lst = heappop(heap)
            node = ListNode(val)
            cur.next = node
            cur = cur.next

            if lst.next:
                heappush(heap,(lst.next.val,i, lst.next))

        return head.next