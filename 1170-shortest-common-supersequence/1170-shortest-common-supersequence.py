class Solution:
    def shortestCommonSupersequence(self, text1: str, text2: str) -> str:
        n, m = len(text1), len(text2)
        dp = [[[0, ""] for i in range(m + 1)] for j in range(n + 1)]
        
        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    dp[i][j] = [1 + dp[i - 1][j - 1][0], dp[i - 1][j - 1][1] + text1[i]]
                else:
                    if dp[i - 1][j][0] > dp[i][j - 1][0]:
                        dp[i][j] = dp[i - 1][j].copy()
                    else:
                        dp[i][j] = dp[i][j - 1].copy()

            
        _, common_long = dp[-2][-2]

        p1, p2, p3 = 0, 0, 0
        new = []

        while p1 < len(text1) and p2 < len(text2) and p3 < len(common_long):
            if (text1[p1] == text2[p2]) and (text1[p1] == common_long[p3]):
                new.append(text1[p1])
                p1 += 1
                p2 += 1
                p3 += 1
            else:
                if text1[p1] != common_long[p3]:
                    new.append(text1[p1])
                    p1 += 1
                if text2[p2] != common_long[p3]:
                    new.append(text2[p2])
                    p2 += 1   
                
        while p1 < len(text1):
            new.append(text1[p1])
            p1 += 1
        
        while p2 < len(text2):
            new.append(text2[p2])
            p2 += 1


        
        return "".join(new)



