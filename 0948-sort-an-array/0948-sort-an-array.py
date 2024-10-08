class Solution:
    def merge(self, a1, a2):
        i, j, new, n, m = 0, 0, [], len(a1), len(a2)
        
        while i < n and j < m:
            if a1[i] > a2[j]:
                new.append(a2[j])
                j += 1
            else:
                new.append(a1[i])
                i += 1
            
        
        while i < n:
            new.append(a1[i])
            i += 1
        
        while j < m:
            new.append(a2[j])
            j += 1
        
        return new
        
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)
        
        
        