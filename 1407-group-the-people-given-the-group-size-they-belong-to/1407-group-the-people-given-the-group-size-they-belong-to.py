class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        n = len(groupSizes)
        freq = [[] for i in range(n+1)]
        ans = []
        for idx, val in enumerate(groupSizes):
            freq[val].append(idx)

            if len(freq[val]) == val:
                ans.append(freq[val])
                freq[val] = []
        
        return ans
