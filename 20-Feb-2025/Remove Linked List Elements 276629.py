# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev=ListNode()
        cur=head
        head=prev
        while cur:
            while cur and cur.val==val:
                cur=cur.next
            prev.next=cur
            prev=prev.next

            if cur:
                cur=cur.next

        return head.next