class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n,m=len(grid),len(grid[0])
        def check(i,j):
            while i<n and j<m:
                if grid[i][j] ==1:
                    if j+1==m or grid[i][j+1]==-1 :
                        return -1
                    i+=1
                    j+=1
                elif grid[i][j] == -1:
                    if j-1 < 0 or grid[i][j-1]==1:
                        return -1
                    i+=1
                    j-=1
            return j
        return [check(0,i) for i in range(m)]
        
                    