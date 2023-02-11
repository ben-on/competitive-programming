class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red=defaultdict(list)
        blue=defaultdict(list)
        for i in redEdges:
            red[i[0]].append(i[1])
        for i in blueEdges:
            blue[i[0]].append(i[1])
        ans=[float("inf")]*n
        qu=deque([[0,None]])
        depth=0
        vis=set()
        while qu:
            r=len(qu)
            for _ in range(r):
                temp=qu.popleft()
                ans[temp[0]]=min(ans[temp[0]], depth)
                if temp[1]=='r':
                    for nb in red[temp[0]]:
                        if (nb,'r') not in vis:
                            qu.append([nb,'b'])
                            vis.add((nb,'r'))
                elif temp[1]=='b':
                    for nb in blue[temp[0]]:
                        if (nb,'b') not in vis:
                            qu.append([nb,'r'])
                            vis.add((nb,'b'))
                else:
                    for nb in red[temp[0]]:
                        qu.append([nb,'b'])
                        vis.add((nb,'r'))
                    for nb in blue[temp[0]]:
                        qu.append([nb,'r'])
                        vis.add((nb,'b'))
            depth+=1
        return [i if i!=float('inf') else -1 for i in ans]
        
        