class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        vis = set()
        cur = []
        ans = []

        def back(i = 0):
            if i == len(nums):
                ans.append(cur.copy())
                return
            
            for idx,num in enumerate(nums):
                if idx not in vis:
                    vis.add(idx)
                    cur.append(nums[idx])
                    
                    back(i + 1)

                    vis.remove(idx)
                    cur.pop()
        back()

        return ans



        