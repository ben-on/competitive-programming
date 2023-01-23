class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n ==1:
            return 1
        dct = defaultdict(list)
        dct2 = defaultdict(list)
        for v1,v2 in trust:
            dct[v2].append(v1)
            dct2[v1].append(v2)
        # print(dct,dct2)
        for i in dct:
            if len(dct[i]) == n-1 and dct2[i] == []:
                return i
        return -1