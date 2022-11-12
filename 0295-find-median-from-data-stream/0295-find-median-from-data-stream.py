class MedianFinder:

    def __init__(self):
        self.first = []
        self.second = []
    def addNum(self, num: int) -> None:
        heapq.heappush(self.first,-1*num)
        if self.first and self.second and -1*self.first[0] > self.second[0]:
            temp = -1 *heapq.heappop(self.first)
            heapq.heappush(self.second,temp)
        if len(self.first) > len(self.second)+1:
            temp = -1 *heapq.heappop(self.first)
            heapq.heappush(self.second,temp)
        if len(self.first)+1 < len(self.second):
            temp = -1* heapq.heappop(self.second)
            heapq.heappush(self.first,temp)
        

    def findMedian(self) -> float:
        # print(self.first,self.second)
        if len(self.first)>len(self.second):
            return -1*self.first[0]
        if len(self.first)<len(self.second):
            return self.second[0] 
        return ((-1*self.first[0])+self.second[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()