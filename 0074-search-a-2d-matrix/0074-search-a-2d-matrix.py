class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1
        

        if r < 0:
            return False
        row = r
        l, r = 0, len(matrix[row]) - 1

        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        if r < 0:
            return False
        
        return matrix[row][r] == target
