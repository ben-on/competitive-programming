# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, BinaryMatrix: 'BinaryMatrix') -> int:
        def getFirstIndex(BinaryMatrix,rowIndex,m):
            low,high=0,m-1
            while low<=high:
                mid=(low+high)>>1
                if BinaryMatrix.get(rowIndex, mid)==0:
                    low=mid+1
                else:
                    high=mid-1
            return low if low<m else float("inf")

        def solve(BinaryMatrix):
            ans=float("inf")
            n,m=BinaryMatrix.dimensions()
            for i in range(n):
                ans=min(ans,getFirstIndex(BinaryMatrix,i,m))
            return ans if ans!=float("inf") else -1
        return solve(BinaryMatrix)