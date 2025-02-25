# Problem: Design Browser History - https://leetcode.com/problems/design-browser-history/description/

class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur=Node(homepage)
        

    def visit(self, url: str) -> None:
        node=Node(url)
        node.prev=self.cur
        self.cur.next=node
        self.cur=self.cur.next

    def back(self, steps: int) -> str:
        while steps>0 and self.cur.prev:
            self.cur=self.cur.prev
            steps-=1
        
        return self.cur.val

    def forward(self, steps: int) -> str:
        while steps>0 and self.cur.next:
            self.cur=self.cur.next
            steps-=1

        return self.cur.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)