# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                slow=head
                pos=0
                while True:
                    if slow==fast:
                        return slow
                    slow=slow.next
                    fast=fast.next
                    pos+=1
        return None
        