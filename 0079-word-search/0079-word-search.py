class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        moves = [(1,0),(0,1),(-1,0),(0,-1)]
        n,m,l = len(board),len(board[0]),len(word)
        
        def find(x,y):
            stk = [(x,y,0,[(x,y)])]
            while stk:
                tx,ty,idx,p = stk.pop()
                for mx, my in moves:
                    nx = mx+tx
                    ny = my+ty
                    if idx+1 < l:
                        if 0 <= nx < n and 0<= ny < m and board[nx][ny] == word[idx+1] and (nx,ny) not in p:
                            stk.append((nx,ny,idx+1,p+[(nx,ny)]))
                        
                    elif board[tx][ty]==word[-1]:
                        return True
            return False
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if find(i,j):
                        return True
        return False
                