# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, mat: 'BinaryMatrix') -> int:
        rows,cols = mat.dimensions()
        minCol = float('inf')
        col = cols-1
        for row in range(rows):
            while col >= 0:
                if mat.get(row,col) == 0:
                    break
                if mat.get(row,col) == 1:
                    minCol = min(minCol,col)
                col -= 1
        return minCol if minCol != float('inf') else -1