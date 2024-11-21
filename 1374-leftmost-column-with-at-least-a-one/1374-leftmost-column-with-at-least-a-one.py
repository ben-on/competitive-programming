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
        for row in range(rows):
            if mat.get(row,cols-1) == 1:
                start = 0
                end = cols-1
                while start <= end:
                    mid = start + (end-start)//2
                    if mat.get(row,mid) == 1:
                        end = mid - 1
                    else:
                        start = mid + 1
                if start < cols:
                    minCol = min(minCol,start)
        return minCol if minCol != float('inf') else -1
        