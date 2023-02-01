class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        nums = set(nums)
        nums = [i for i in nums if i != 0]
        heapify(nums)
        while nums:
            cur = heappop(nums)
            for i in range(len(nums)):
                nums[i]-=cur
                
            ans +=1
        return ans