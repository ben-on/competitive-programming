class Solution:
    dp={}
    def tribonacci(self, n: int) -> int:
        if n==1 or n==0:
            return n
        if n==2:
            return 1
        if n in self.dp:
            return self.dp[n]
        else:
            self.dp[n]=self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
            return self.dp[n]
        