class Solution:
    def minDifficulty(self, jobDifficulties: List[int], days: int) -> int:
        n = len(jobDifficulties)
        @cache
        def check(i: int, days: int) -> int:
            if days == 0 or n - i < days:
                return -1
            if days == 1:
                return max(jobDifficulties[i:])
            res = math.inf
            curr_max = -math.inf
            for j in range(i, n - days + 1):
                curr_max = max(curr_max, jobDifficulties[j])
                res = min(res, curr_max + check(j + 1, days - 1))
            return res
        return check(0, days)