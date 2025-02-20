# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left=ListNode(next=head)
        right=head
        head=left
        while right and n>0:
            right=right.next
            n-=1
        
        while right:
            left=left.next
            right=right.next
        
        left.next=left.next.next

        return head.next
