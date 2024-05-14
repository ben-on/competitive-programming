class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.leaders = []
        self.times = times
        
        freq = {}
        cur_max = 0
        cur_lead = 0
        for i in persons:
            freq[i] = freq.get(i, 0) + 1
            
            if cur_max <= freq[i]:
                cur_max = freq[i]
                cur_lead = i
            
            self.leaders.append(cur_lead)
            
        
        

    def q(self, t: int) -> int:
        left = 0
        right = len(self.times) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if self.times[mid] > t:
                right = mid - 1
            else:
                left = mid + 1
        
        return self.leaders[right]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)