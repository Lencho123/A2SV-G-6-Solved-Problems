# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # first find the middle of the linked list
        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        # create reversed list starting from middle of the list(middle)
        prev=None
        left=slow
        while slow:
            slow=slow.next
            left.next=prev
            prev=left
            left=slow

        
        # check wether they are palindome
        while head and prev:
            if head.val!=prev.val:
                return False
            head=head.next
            prev=prev.next
        
        return True