class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        def quick(l,r):
            piv ,p= nums[r], l
            for i in range(l,r):
                if nums[i]<=piv:
                    nums[i], nums[p] = nums[p] , nums[i]
                    p+=1
            nums[r],nums[p] = nums[p], nums[r]
                
            if p < k:
                return quick(p+1,r)
            if p > k:
                return quick(l,p-1)
            return nums[p]
        return quick(0, len(nums)-1)