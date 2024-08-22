class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        dungeon[-1][-1] = min(dungeon[-1][-1], 0)
        for i in range(n - 1, -1,-1):
            for j in range(m - 1, -1 , -1):
                if (i,j) == (n - 1,m - 1):
                    continue
                down = dungeon[i + 1][j] if  i + 1 < n else -float('inf')
                right = dungeon[i][j + 1] if  j + 1 < m else -float('inf')
                
                dungeon[i][j] = min(0, dungeon[i][j] + max(down, right))


        ans = abs(dungeon[0][0])     
        
        return ans + 1



