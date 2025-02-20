# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less=ListNode()
        great=ListNode()
        l=less
        g=great

        cur=head
        n=6
        while cur and n>0:
            node=ListNode(cur.val)
            if cur.val<x:
                less.next=node
                less=less.next
            else:
                great.next=node
                great=great.next
            cur=cur.next
            
        if g.next:
            less.next=g.next
            
        return l.next