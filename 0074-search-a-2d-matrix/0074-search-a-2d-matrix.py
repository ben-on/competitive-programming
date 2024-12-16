class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        right = len(matrix[0]) - 1

        while left < len(matrix) and right >= 0:
            if matrix[left][right] == target:
                return True
            elif matrix[left][right] > target:
                right -= 1
            else:
                left += 1
            

        
        return False
