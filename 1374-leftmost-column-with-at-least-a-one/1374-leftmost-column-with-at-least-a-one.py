# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix():
#    def __init__(mat, row, col):
#       self.mat = mat
#       self.row = row
#       self.col = col   
#    def get(self, row: int, col: int) -> int:
#        return self.mat[row][col]
#    def dimensions(self) -> list[]:
 #       return [self.row, self.col]



class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        row, col = binaryMatrix.dimensions()
        ans = 101
        
        for i in range(row):
            l, r = 0, col - 1
            
            while l <= r:
                mid = (l + r) // 2
                val = binaryMatrix.get(i, mid)
                
                if val == 1:
                    ans = min(ans, mid)
                    r = mid - 1
                else:
                    l = mid + 1
        
        return ans if ans != 101 else -1