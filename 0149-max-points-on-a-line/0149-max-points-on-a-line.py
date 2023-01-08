class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        n = len(points)
        ans = -float('inf')
        for i,(x1,y1) in enumerate(points):
            slopes = []
            
            for j,(x2,y2) in enumerate(points):
                if i == j:
                    continue
                if x1-x2:
                    m = (y1-y2)/(x1-x2) 
                else:
                    m = "vert"
                slopes.append(m)
                
            curmax = max(Counter(slopes).values())
            ans = max(curmax,ans)
        return ans+1
            
                
                
            