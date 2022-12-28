class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        lst = [capacity[i]- rocks[i] for i in range(len(rocks))]
        orig = len(lst)
        heapq.heapify(lst)
        while additionalRocks and lst:
            temp = heapq.heappop(lst)
            if additionalRocks >= temp:
                additionalRocks -= temp
            else:
                heapq.heappush(lst,temp)
                break
        return orig - len(lst)