class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1,len(nums)):
            nums[i] +=nums[i-1]
        ans = []
        # print(nums)
        for q in queries:
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left+right)//2
                if nums[mid] > q:
                    right = mid -1
                else:
                    left = mid + 1
            ans.append(left)
        return ans
                    
                    
            