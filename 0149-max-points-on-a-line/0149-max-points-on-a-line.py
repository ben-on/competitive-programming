class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        n = len(points)
        ans = -float('inf')
        for i in range(n):
            slopes = []
            x1,y1 = points[i][0],points[i][1]
            for j in range(n):
                if i == j:
                    continue
                x2,y2 = points[j][0],points[j][1]
                if x1-x2:
                    m = (y1-y2)/(x1-x2)
                else:
                    m = "vert"
                slopes.append(m)
            # print(points[i],slopes)
            curmax = max(Counter(slopes).values())
            # print(curmax)
            ans = max(curmax,ans)
        # print()
        return ans+1
            
                
                
            