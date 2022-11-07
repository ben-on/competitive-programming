class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = list(str(num))
        for i in range(len(str(num))):
            if str(num)[i]=="6":
                ans[i]='9'
                break
                
        return "".join(ans)
        