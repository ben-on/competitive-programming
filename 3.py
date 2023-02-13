class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        pre = 0
        ans = 0
        for val in nums:
            pre +=val
            ans += dic.get(pre%k,0)
            dic[pre%k] = dic.get(pre%k,0) + 1
        return ans
            
