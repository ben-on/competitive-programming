class Solution:
    def minimumRounds(self, tasks):
        frequecy = Counter(tasks).values()
        return -1 if 1 in frequecy else sum((a + 2) // 3 for a in frequecy)
                
                
                
            