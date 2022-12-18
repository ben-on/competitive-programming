class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        ans = [0]*len(temp)
        stk = [0]
        for i in range(len(temp)):
            while stk and temp[i] > temp[stk[-1]]:
                tempo = stk.pop()
                ans[tempo] = i - tempo
            stk.append(i)
        return ans
            