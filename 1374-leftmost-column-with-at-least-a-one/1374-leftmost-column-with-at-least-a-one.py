# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, BinaryMatrix: 'BinaryMatrix') -> int:
        n,m=BinaryMatrix.dimensions()
        i,j=0,m-1
        while i<n and j>=0:
            if BinaryMatrix.get(i, j)==0:
                i+=1
            else:
                j-=1
        return j+1 if j<m-1 else -1