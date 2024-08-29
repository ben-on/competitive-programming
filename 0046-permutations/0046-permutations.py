class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        vis = 0
        cur = []
        ans = []

        def back(i = 0):
            nonlocal vis
            if i == len(nums):
                ans.append(cur.copy())
                return
            
            for idx,num in enumerate(nums):
                if  not ((1 << idx) & vis ):
                    vis = vis | (1 << idx)
                    cur.append(nums[idx])
                    
                    back(i + 1)

                    vis = vis & (~(1 << idx))
                    cur.pop()
        back()

        return ans



        