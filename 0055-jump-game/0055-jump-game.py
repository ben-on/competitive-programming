class Solution:
    
    def canJump(self, nums: List[int]) -> bool:
        lg = len(nums)
        curr = lg - 1
        for i in range(lg - 2, -1, -1):
            if nums[i] >= curr - i:
                curr = i  
        return curr == 0
        # @cache
        # def ch(idx):
        #     if idx>=len(nums)-1 :
        #         return True
        #     ans=False
        #     for i  in range(1,nums[idx]+1):
        #         if i in range(len(nums)):
        #             ans=ans or ch(idx+i)
        #     return ans
        # return ch(0)
                
        