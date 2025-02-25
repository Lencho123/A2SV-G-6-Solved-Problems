# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode()

        cur1=l1
        cur2=l2
        tail=head
        cary=0

        while cur1 or cur2:
            v1,v2=0,0
            if cur1:
                v1=cur1.val
                cur1=cur1.next
            if cur2:
                v2=cur2.val
                cur2=cur2.next
            
            sm=v1+v2+cary
            if sm > 9:
                sm=sm-10
                cary=1
            else:
                cary=0
            
            node=ListNode(sm)
            tail.next=node
            tail=tail.next
        
        if cary:
            node=ListNode(cary)
            tail.next=node

        return head.next