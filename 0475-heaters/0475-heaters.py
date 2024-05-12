class Solution:
    def check_radius(self,radi, houses, heaters):
        left = 0
        n = len(houses)
        for right in range(len(heaters)):
            while left < n and abs(heaters[right] - houses[left]) <= radi:
                left += 1
            
        return left == n
            
            
            
            
            
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # print(self.check_radius(, houses, heaters))
        
        houses.sort()
        heaters.sort()
        
        left = 0
        right = max(heaters[-1], houses[-1])
        
        while left <= right:
            mid = ceil((left + right) / 2)
            
            if self.check_radius(mid, houses, heaters):
                right = mid - 1
            else:
                left = mid + 1
        
        return left
