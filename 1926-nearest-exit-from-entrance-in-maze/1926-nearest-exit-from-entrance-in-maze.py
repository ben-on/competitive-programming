class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        que = deque([entrance])
        n,m = len(maze), len(maze[0])
        moves = [(1,0),(-1,0),(0,1),(0,-1)]
        vis = {tuple(entrance)}
        dp = 0
        b = False
        while que :
            r = len(que)
            for _ in range(r):
                x,y = que.popleft()
                if [x,y]!= entrance:
                    if x == n-1 or y == m-1 or x == 0 or y ==0 :
                        b = True
                        return dp
                for mx,my in moves:
                    nx = x+mx
                    ny = y + my
                    if (nx,ny) not in vis and 0<=nx <n and 0<=ny<m and maze[nx][ny]=='.':
                        que.append([nx,ny])
                        vis.add((nx,ny))
            
            dp+=1
        return dp if b else -1
                    