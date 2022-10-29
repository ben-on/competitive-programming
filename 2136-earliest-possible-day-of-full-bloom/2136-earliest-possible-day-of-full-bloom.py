class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        result = 0
        for grow, plant in sorted(zip(growTime, plantTime)):
            result = max(result, grow) + plant
        return result