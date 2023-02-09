class Solution:
    def maximumSwap(self, num: int) -> int:
        new = sorted(str(num),reverse=True)
        num = list(str(num))
        for i in range(len(new)):
            if new[i] != num[i]:
                swap = None
                for j in range(i,len(new)):
                    if num[j] == new[i]:
                        swap = j
                num[i],num[swap] = num[swap],num[i]
                break
        return int("".join(num))