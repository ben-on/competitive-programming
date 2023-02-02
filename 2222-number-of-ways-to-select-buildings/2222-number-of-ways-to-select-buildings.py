class Solution:
    def numberOfWays(self, s: str) -> int:
        fwd = []
        dic = {'0':0,'1':0}
        n = len(s)
        for i in range(n):
            dic[s[i]]+=1
            fwd.append([dic['0'],dic['1']])
        back = [None]*n
        dic = {'0':0,'1':0}
        n = len(s)
        for i in range(n-1,-1,-1):
            dic[s[i]]+=1
            back[i] = [dic['0'],dic['1']]
        ans = 0
        for i in range(1,n-1):
            if s[i] == '0':
                ans += fwd[i][1]*back[i][1]
            else:
                ans += fwd[i][0]*back[i][0]
        return ans
        
            