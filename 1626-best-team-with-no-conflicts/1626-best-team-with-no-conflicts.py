class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        agesSc = list(sorted((a,s) for s,a in zip(scores,ages)))
        dp = [agesSc[i][1] for i in range(len(agesSc))]
        for i in range(1,len(agesSc)):
            for j in range(i):
                if agesSc[j][0] == agesSc[i][0]:
                    
                    dp[i] = max(dp[i],dp[j]+agesSc[i][1])
                elif agesSc[j][0] != agesSc[i][0]:
                    if agesSc[i][1] >= agesSc[j][1]:
                        dp[i] = max(dp[i],dp[j]+agesSc[i][1])
        return max(dp)