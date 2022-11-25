class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        A = [0]+A
        res = [0]*len(A)
        stk = [0]
        for i in range(len(A)):
            while A[stk[-1]] > A[i]:
                stk.pop() 
            j = stk[-1]
            res[i] = res[j] + (i-j)*A[i]
            stk.append(i)
        return sum(res) % (10**9+7)
            