class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        one = int(bin(nums[0])[2:] + bin(nums[1])[2:] + bin(nums[2])[2:],2)
        two = int(bin(nums[0])[2:] + bin(nums[2])[2:] + bin(nums[1])[2:], 2)
        three = int(bin(nums[1])[2:] + bin(nums[0])[2:] + bin(nums[2])[2:], 2)
        four = int(bin(nums[1])[2:] + bin(nums[2])[2:] + bin(nums[0])[2:],2)
        five = int(bin(nums[2])[2:] + bin(nums[0])[2:] + bin(nums[1])[2:],2)
        six = int (bin(nums[2])[2:] + bin(nums[1])[2:] + bin(nums[0])[2:],2)
        
        return max([one, two, three, four, five, six])
        
        