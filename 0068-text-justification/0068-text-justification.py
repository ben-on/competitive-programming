class Solution:
    def Corner(self,L,maxWidth):
        n = len(L)
        spaces = [1 for i in range(n-1)] + [0]
        s = "".join(L[i] + " "*spaces[i] for i in range(n))
        return s + " "*(maxWidth-len(s))
    
    def Normal(self,L, tolspace,n):
        space, r = divmod(tolspace, n-1)
        spaces = [space+1 if i < r else space for i in range(n-1)] + [0]
        return "".join(L[i] + " "*spaces[i] for i in range(n))
    
    def fullJustify(self, words, maxWidth):

        ans, curr, temp = [], 0, 0
        for i in range(len(words)):
            le = len(words[i]) 
            if curr + le <= maxWidth:
                curr += le +1
                continue
            n = i - temp
            if n==1:
                ans.append(self.Corner(words[temp:i],maxWidth))
            else:
                ans.append(self.Normal(words[temp:i], maxWidth-curr+n,n))
            temp, curr = i, le + 1
        return ans + [self.Corner(words[temp:],maxWidth)]
