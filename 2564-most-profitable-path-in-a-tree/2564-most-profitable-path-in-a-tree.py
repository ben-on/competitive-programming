class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges) + 1
        graph = defaultdict(list)

        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        
        parent = [None] * n
        ans = -float('inf')
        que = deque([0])  
        
        while que:
            r = len(que)
            for i in range(r):
                cur = que.popleft()

                for child in graph[cur]:
                    if parent[cur] != child:
                        que.append(child)
                        parent[child] = cur

        seconds = [float('inf')] * n
        cnt = 0
        while bob != None:
            seconds[bob] = cnt
            cnt += 1
            bob = parent[bob]
        
        cnt = 0
        que = deque([[0, amount[0]]])  
        
        while que:
            r = len(que)
            for i in range(r):
                cur, cur_score = que.popleft()
                if cur != 0 and len(graph[cur]) == 1:
                    ans = max(ans, cur_score)
                for child in graph[cur]:
                    if parent[cur] != child:
                        if seconds[child] < cnt + 1:
                            que.append([child, cur_score])
                        elif seconds[child] > cnt + 1:
                            que.append([child, cur_score + amount[child]])
                        else:
                            que.append([child, cur_score + (amount[child]) //2 ])

                        
                        
            
            cnt += 1
        
        return ans


