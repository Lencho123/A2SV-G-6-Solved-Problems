# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) > len(self.min_heap):
            heappush(self.min_heap, num)
        else:
            heappush(self.max_heap, -num)

        if self.min_heap and self.max_heap:
            a,b = heappop(self.min_heap), -heappop(self.max_heap)

            mx,mn = min(a,b),max(a,b)
            heappush(self.min_heap, mn)
            heappush(self.max_heap, -mx)

    def findMedian(self) -> float:
        mil, mxl= len(self.min_heap),len(self.max_heap)
        if mil > mxl:
            return self.min_heap[0]
        elif mil < mxl:
            return -self.max_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()