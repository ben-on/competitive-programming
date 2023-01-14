class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = defaultdict(set)
        for i in range(len(s1)):
            graph[s1[i]].add(s2[i])
            graph[s2[i]].add(s1[i])
        ans = []
        # print(graph)
        for i in range(len(baseStr)):
            mm= 'z'
            vis = {baseStr[i]}
            stk = [baseStr[i]]
            while stk:
                temp = stk.pop()
                mm = min(mm,temp)
                for nb in graph[temp]:
                    if nb not in vis:
                        stk.append(nb)
                        vis.add(nb)
            ans.append(mm)
        return "".join(ans)