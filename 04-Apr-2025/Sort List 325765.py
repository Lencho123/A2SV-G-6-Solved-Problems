# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergeSort(head):
            l = length(head)
            if l<=1:
                return head

            prev = None
            cur = head
            pos = 0
            while pos < l//2:
                prev = cur
                cur = cur.next
                pos+=1
            prev.next = None
            
            left = mergeSort(head)
            right = mergeSort(cur)

            return merge(left,right)
        
        def merge(left,right):
            merged = ListNode(0)
            ptr = merged
            l=left
            r=right

            while l or r:
                if not l:
                    ptr.next = r
                    break
                if not r:
                    ptr.next = l
                    break
                
                if l.val < r.val:
                    ptr.next = l
                    ptr = ptr.next
                    l = l.next
                else:
                    ptr.next = r
                    ptr = ptr.next
                    r = r.next
            return merged.next

        def length(arr):
            p = arr
            l = 0 
            while p:
                l+=1
                p=p.next
            return l
        
        return mergeSort(head)