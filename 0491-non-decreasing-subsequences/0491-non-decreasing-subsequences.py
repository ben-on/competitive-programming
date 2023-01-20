class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans =[]
        @cache
        def back(lst,idx):
            if idx >= len(nums)-1:
                if len(lst)>= 2:
                    ans.append(lst)
                return
            # print(lst)
            if nums[idx+1] < lst[-1]:
                back(lst,idx+1)
                back((nums[idx+1],),idx+1)
                return 
            back(lst+(nums[idx+1],),idx+1)
            back((nums[idx+1],),idx+1)
            back(lst,idx+1)
            return
        back((nums[0],),0)
        return list(set(ans))
        # return list(set([tuple(i) for i in ans]))