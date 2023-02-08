class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        lst=[]
        nums.sort()
        for i in range(len(nums)) :
            if lst and nums[i]==lst[-1][0] :
                lst[-1][1]+=1
            else :
                lst.append([nums[i],1])
        if len(lst) >=3 :
            return lst[-3][0]
        return lst[-1][0]