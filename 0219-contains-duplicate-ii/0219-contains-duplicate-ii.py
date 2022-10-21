class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        prev=set()
        left=0
        for i in nums:
            if i in prev:
                return True
            prev.add(i)
            if len(prev)>k:
                prev.remove(nums[left])
                left+=1
        return False
                