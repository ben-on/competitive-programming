class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        dictt = {}
        for i, route in enumerate(routes): 
            for x in route: 
                dictt.setdefault(x, []).append(i)
        
        ans = 1 
        seen = {source}
        queue = [source]
        while queue: 
            newq = []
            for x in queue: 
                if x == target: return ans - 1
                for i in dictt[x]: 
                    for xx in routes[i]: 
                        if xx not in seen: 
                            seen.add(xx)
                            newq.append(xx)
                    routes[i] = []
            ans += 1
            queue = newq
        return -1 