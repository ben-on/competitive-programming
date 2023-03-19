class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        """
        - sort the given array
        - choose the last two and the first two numbers
        - make the first two numbers maxx and calculate the score
        - make the last two numbers min and calculate the score
        - choose the min of the two scores
        
        
        """
        
        nums.sort()
        return min(nums[-3]-nums[0],nums[-2]-nums[1],nums[-1]-nums[2])