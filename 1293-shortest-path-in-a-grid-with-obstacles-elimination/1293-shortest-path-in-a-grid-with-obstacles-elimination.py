class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n,m = len(grid), len(grid[0])
        c = 0
        vis = set()
        que = deque([(0,0,k)])
        vis.add((0,0,k))
        moves = [(1,0),(0,1),(-1,0),(0,-1)]
        while que:
            r = len(que)
            # print(que)
            for _ in range(r):
                temp = que.popleft()
                if (temp[0],temp[1]) == (n-1,m-1):
                    return c
                for x,y in moves:
                    # print(x,y)
                    mx = x+ temp[0]
                    my = y + temp[1]
                    # print(mx,my)
                    if 0<= mx < n and 0<= my < m and temp[2] >= 0:
                        if (mx,my,temp[2]-grid[mx][my]) not in vis:
                            que.append( (mx,my,temp[2]-grid[mx][my]) )
                            vis.add((mx,my,temp[2]-grid[mx][my]))
            c+=1
        return -1