class Solution:
    def numTilings(self, N):
        a, b, c = 0, 1, 1
        for i in range(N - 1): a, b, c = b, c, (c + c + a) % int(1e9 + 7)
        return c
        # @cache
        # def memo(i):
        #     if i < 0:
        #         return 0
        #     if i == 0:
        #         return 1
        #     return memo(i-1)+memo(i-2)+(memo(i-3))
        # return memo(n) % (10**9 + 7)