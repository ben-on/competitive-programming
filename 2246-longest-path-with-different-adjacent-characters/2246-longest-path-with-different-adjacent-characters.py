class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        for i in range(len(parent)):
            if parent[i] != -1:
                graph[parent[i]].append(i)
                graph[i].append(parent[i])
        @cache
        def dfs(node, parent):
            ret = 1
            for neighbor in graph[node]:
                if neighbor == parent: continue
                if s[neighbor] != s[node]:
                    ret = max(ret, dfs(neighbor, node) + 1)
            return ret
        return max(dfs(i, -1) for i in range(len(parent)))