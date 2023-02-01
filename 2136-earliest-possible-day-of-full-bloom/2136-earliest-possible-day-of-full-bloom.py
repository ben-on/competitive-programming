class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        result = 0
        # print(sorted(zip(growTime, plantTime)))
        for grow, plant in sorted(zip(growTime, plantTime)):
            # print("result",result,"grow",grow,"plant",plant)
            
            result = max(result, grow) + plant
            # print(result)
        return result