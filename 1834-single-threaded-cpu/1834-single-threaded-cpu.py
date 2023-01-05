class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ptr = 0
        n = len(tasks)
        arr = [[*tasks[i], i] for i in range(n)]
        arr.sort()
        heap = []
        current = 0
        ans = []
        while ptr < n:
            
            current = max(arr[ptr][0], current)
            while ptr < n and arr[ptr][0] <= current:
                heappush(heap, (arr[ptr][1], arr[ptr][2]))
                ptr += 1
            
            while heap and (ptr >= n or arr[ptr][0] > current):
                dur, idx = heappop(heap)
                current += dur
                ans.append(idx)
            
            
        return ans