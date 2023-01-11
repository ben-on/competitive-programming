class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pre = [0]
        for i in nums:
            if i == 0:
                pre.append(pre[-1]-1)
            else:
                pre.append(pre[-1]+1)
        dic = {}
        ans = 0
        for i in range(len(pre)):
            if pre[i] in dic:
                ans = max(ans,i-dic[pre[i]])
            else:
                dic[pre[i]] = i
        return ans