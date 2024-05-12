class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans = []
        
        for i in range(len(grid)-2):
            temp = []
            for j in range(len(grid[0])-2):
                mx1 = max(grid[i][j:j+3])
                mx2 = max(grid[i+1][j:j+3])
                mx3 =  max(grid[i+2][j:j+3])
                
                temp.append(max([mx1, mx2, mx3]))
            ans.append(temp)
        
        return ans
                
                