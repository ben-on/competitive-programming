class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        ptr1 = 0
        ptr2 = 0
        n,m = len(nums1),len(nums2)
        while ptr1 < n and ptr2 <m:
            if nums1[ptr1] < nums2[ptr2]:
                ptr1 +=1
            elif nums1[ptr1] > nums2[ptr2]:
                ptr2 +=1
            else:
                return nums1[ptr1]
        return -1