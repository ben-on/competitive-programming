class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        d = Counter(nums)
        g_max = 0
        
        for key in d:
            if key == k:
                continue
            mm = 0
            running = 0
            mx = 0

            for num in nums:
                if num == key:
                    running += 1
                elif num == k:
                    running -= 1
                

                mx = max(mx, running - mm)
                mm = min(mm, running)
                
            
            g_max = max(g_max, mx)
            
        
        return g_max + d.get(k, 0)
