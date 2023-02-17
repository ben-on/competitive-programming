class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        remove = 0
        last = 0
        for i in range(1,n):
            if intervals[i][1] <= intervals[last][1] :
                remove +=1
                continue
            elif intervals[i][0] == intervals[last][0]:
                remove+=1
            last = i
            
        return n-remove