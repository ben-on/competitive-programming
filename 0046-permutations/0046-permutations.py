class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        ans = []
        cur = []

        def back():
            if len(visited) == len(nums):
                ans.append(cur.copy())
                return
            
            for num in nums:
                if num not in visited:
                    cur.append(num)
                    visited.add(num)
                    back()
                
                    cur.pop()
                    visited.remove(num)
        back()
        return ans
            


        