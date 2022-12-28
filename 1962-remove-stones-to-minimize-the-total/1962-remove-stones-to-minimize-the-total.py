class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-i for i in piles]
        heapq.heapify(piles)
        for i in range(k):
            temp = -1*heapq.heappop(piles)
            heapq.heappush(piles,-1*(temp-temp//2))
        return -1*sum(piles)
        