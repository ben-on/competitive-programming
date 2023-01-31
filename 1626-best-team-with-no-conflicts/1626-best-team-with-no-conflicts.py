class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        score_ages = list(sorted((a,s) for s,a in zip(scores,ages)))
        
        
        dp = [score_ages[i][1] for i in range(len(score_ages))]
        for i in range(1,len(score_ages)):
            for j in range(i):
                if score_ages[j][0] == score_ages[i][0]:
                    
                    dp[i] = max(dp[i],dp[j]+score_ages[i][1])
                elif score_ages[j][0] != score_ages[i][0]:
                    if score_ages[i][1] >= score_ages[j][1]:
                        dp[i] = max(dp[i],dp[j]+score_ages[i][1])
        return max(dp)