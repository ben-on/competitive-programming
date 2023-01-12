class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums =[-1*i for i in nums]
        heapq.heapify(nums)
        score = 0
        for i in range(k):
            temp = -1*heapq.heappop(nums)
            score += temp
            heapq.heappush(nums,-1*(ceil(temp/3)))
        return score