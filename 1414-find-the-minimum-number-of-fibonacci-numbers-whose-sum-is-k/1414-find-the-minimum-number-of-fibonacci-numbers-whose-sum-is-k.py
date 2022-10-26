class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        seq = [1,1]
        while seq[-1]<=k:
            seq.append(seq[-1]+seq[-2])
        c=0
        for i in range(len(seq)-1,-1,-1):
            if k-seq[i]>=0:
                k-=seq[i]
                c+=1
            if k==0:
                return c