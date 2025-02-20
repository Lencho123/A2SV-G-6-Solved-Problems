# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre=head
        cur=head

        while cur:
            while cur and cur.val==pre.val:
                cur=cur.next
            pre.next=cur
            pre=pre.next
    
        if pre:
            pre.next=None

        return head