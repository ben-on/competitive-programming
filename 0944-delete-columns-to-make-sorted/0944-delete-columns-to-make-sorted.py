class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        # print(len(strs[0]))
        for i in range(len(strs[0])):
            b = True
            print("yes",i)
            for j in range(1,len(strs)):
                # print(strs[j][i])
                if ord(strs[j][i]) < ord(strs[j-1][i]):
                    b = False
                    break
            if b :
                ans += 1
        return len(strs[0]) - ans