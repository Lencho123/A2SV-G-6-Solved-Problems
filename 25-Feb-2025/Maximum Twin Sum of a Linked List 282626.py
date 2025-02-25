# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        prev=None
        cut=head
        grab=head
        while grab!=slow:
            grab=grab.next
            cut.next=prev
            prev=cut
            cut=grab
        
        # calculate max twin
        mx=0
        while slow:
            mx=max(mx, slow.val+prev.val)
            slow=slow.next
            prev=prev.next

        return mx