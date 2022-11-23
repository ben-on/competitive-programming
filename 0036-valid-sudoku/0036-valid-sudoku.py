class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n,m = len(board), len(board[0])
        for i in range(n):
            s = set()
            for j in range(m):
                if board[i][j] in s:
                    return False
                if board[i][j]!='.':
                    s.add(board[i][j])
        for i in range(m):
            s = set()
            for j in range(n):
                if board[j][i] in s:
                    return False
                if board[j][i]!='.':
                    s.add(board[j][i])
        i = 0
        while i< n:
            j = 0
            while j<m:
                s = set()
                # print(j)
                for k in range(i,i+3):
                    for q in range(j,j+3):
                        if board[k][q] in s:
                            return False
                        if board[k][q] !='.':
                            s.add(board[k][q])
                j+=3
                
            i+=3
        return True
                        
                