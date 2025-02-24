# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, val=0, key=0, prev=None, next=None):
        self.val=[val,key]
        self.prev=prev
        self.next=next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.dct=defaultdict(Node)
        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.prev=self.head

    def get(self, key: int) -> int:
        if key in self.dct:
            # remove
            val=self.dct[key].val[0]
            self.dct[key].prev.next=self.dct[key].next
            self.dct[key].next.prev=self.dct[key].prev

            # add at end
            node=Node(val,key,None,None)
            node.next=self.tail
            node.prev=self.tail.prev
            self.tail.prev.next=node
            self.tail.prev=node
            self.dct[key]=node
            return val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dct:
            # remove
            self.dct[key].prev.next=self.dct[key].next
            self.dct[key].next.prev=self.dct[key].prev
            self.capacity+=1

        # add at end
        node=Node(value,key,None, None)
        node.next=self.tail
        node.prev=self.tail.prev
        self.tail.prev.next=node
        self.tail.prev=node
        self.dct[key]=node
        self.capacity-=1
        # check if capacity exteed
        if self.capacity==-1:
            val,key=self.head.next.val[0], self.head.next.val[1]
            self.head.next.next.prev=self.head
            self.head.next=self.head.next.next

            self.capacity+=1
            self.dct.pop(key)
        # print(self.head.next.val, self.head.next.next.val)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)