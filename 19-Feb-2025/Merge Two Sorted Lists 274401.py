# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merge=ListNode()
        
        cur1=list1
        cur2=list2
        head=merge

        while cur1 and cur2:
            if cur1.val<cur2.val:
                merge.next=cur1
                merge=merge.next
                cur1=cur1.next
            else:
                merge.next=cur2
                merge=merge.next
                cur2=cur2.next
        
        if cur1:
            cur=head
            while cur.next:
                cur=cur.next
            cur.next=cur1
        else:
            cur=head
            while cur.next:
                cur=cur.next
            cur.next=cur2
        
        return head.next