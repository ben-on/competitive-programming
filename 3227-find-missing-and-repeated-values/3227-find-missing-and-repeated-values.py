class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        m = n * n

        freq = {i:0 for i in range(1, m + 1)}

        for row in grid:
            for num in row:
                freq[num] += 1
        
        a = [i for i in freq if freq[i] == 2]
        b = [i for i in freq if freq[i] == 0]

        return a + b