# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n=0
        cur=head
        while cur:
            n+=1
            cur=cur.next
        
        loop=n//k
        cur=head
        new_head=None
        tail=None

        for i in range(loop):
            pre=None
            cut=cur
            for j in range(k):
                cur=cur.next
                cut.next=pre
                pre=cut
                cut=cur
            
            
            if i==0:
                new_head=pre
                tail=new_head
            
            while tail and tail.next:
                tail=tail.next
            
            if i>0:
                tail.next=pre
            
            if i==loop-1:
                while tail and tail.next:
                    tail=tail.next
                tail.next=cur

        return new_head