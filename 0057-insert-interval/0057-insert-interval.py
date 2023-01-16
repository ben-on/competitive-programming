class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        heapq.heapify(intervals)
        heapq.heappush(intervals,newInterval)
        ans = [heapq.heappop(intervals)]
        while intervals:
            temp = heapq.heappop(intervals)
            if temp[0] <= ans[-1][1]:
                # ans[-1][0] = min(temp[0],ans[-1][0])
                ans[-1][1] = max(temp[1],ans[-1][1])
            else:
                ans.append(temp)
        return ans