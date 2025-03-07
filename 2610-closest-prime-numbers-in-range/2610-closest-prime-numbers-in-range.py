class Solution:
    def sieve_of_eratosthenes(self, n):
        primes = [True] * (n + 1) 
        primes[0] = primes[1] = False 

        for i in range(2, int(n**0.5) + 1): 
            if primes[i]:  
                for j in range(i * i, n + 1, i):  
                    primes[j] = False

        return [i for i in range(n + 1) if primes[i]]  

    def closestPrimes(self, left: int, right: int) -> List[int]:
        arr = self.sieve_of_eratosthenes(right)

        n = len(arr)
        ans = [-1, -1, float('inf')]
        for i in range(1,n):
            if arr[i - 1] >= left: 
                if ans[-1] > arr[i] - arr[i - 1] :
                    ans = [arr[i - 1], arr[i], arr[i] - arr[i - 1]]
        return ans[:-1]


