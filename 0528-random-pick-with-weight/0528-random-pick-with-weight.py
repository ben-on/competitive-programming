class Solution:

    def __init__(self, w: List[int]):
        self.arr=[]
        self.s=0
        for i in w:
            self.s+=i
            self.arr.append(self.s)

    def pickIndex(self) -> int:
        n=self.s * random.random()
        return bisect.bisect_left(self.arr,n)
    
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()