class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        graph = defaultdict(list)
        for child,parent in enumerate(parents):
            graph[parent].append(child)
        dp = {}
        def dfs(node):
            if not graph[node]:
                dp[node] = 1
                return 1
            temp = 1
            for nb in graph[node]:
                temp += dfs(nb)
            dp[node] = temp
            return dp[node]
        
        tot = dfs(graph[-1][0])
        # print(tot)
        ans = -float('inf')
        freq = None
        for node in dp:
            if graph[node]:
                score = prod([dp[child] for child in graph[node]])
                left = tot - (sum([dp[child] for child in graph[node]])+1)
                if left:
                    score *= left
            else:
                score = tot-1
            if score > ans:
                ans = score
                freq = 1
            elif score == ans:
                freq +=1
        return freq
            
                