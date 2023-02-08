class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)
        for index, equation in enumerate(equations):
            val = values[index]
            var1, var2 = equation
            graph[var1].append((var2, val))
            graph[var2].append((var1, 1/val))

        answer = []
        for query in queries:
            var1, var2 = query
            evaluation = self.evalEquation(var1, var2, graph, set())
            answer.append(evaluation)

        return answer
    def evalEquation(self, curr_var, target, graph, visited):
        for var, val in graph[curr_var]:

            if var == target:
                return val
            if var not in visited:
                visited.add(var)
                evaluation = self.evalEquation(var, target, graph, visited)
                if evaluation != -1:
                    return evaluation * val

        return -1
    
        