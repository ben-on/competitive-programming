class Solution:
    
            
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK( nums, k):
            goodCt = 0
            Ct = collections.Counter()

            begin = 0
            for end in range(len(nums)):
                if Ct[nums[end]] == 0:
                    k -= 1
                Ct[nums[end]] += 1

                while k < 0:
                    Ct[nums[begin]] -= 1
                    if Ct[nums[begin]] == 0:
                        k += 1

                    begin += 1

                goodCt += end - begin + 1

            return goodCt
        return atMostK(nums, k) - atMostK(nums, k - 1)