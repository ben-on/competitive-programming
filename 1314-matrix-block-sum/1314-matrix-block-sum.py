class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        answer = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(1, n):
                mat[r][c] += mat[r][c - 1]

        for c in range(n):
            for r in range(1, m):
                mat[r][c] += mat[r - 1][c]

        for i in range(m):
            r1, r2 = max(i - k, 0), min(i + k, m - 1)
            for j in range(n):
                c1, c2  = max(j - k, 0), min(j + k, n - 1)

                answer[i][j] = mat[r2][c2] 
                if r1 == 0 and c1 == 0:
                    continue
                elif c1 == 0:
                    answer[i][j] -= mat[r1 - 1][c2]
                elif r1 == 0:
                    answer[i][j] -= mat[r2][c1 - 1]
                else:
                    left_bottom = mat[r2][c1 - 1]
                    left_bottom -= mat[r1 - 1][c1 - 1]
                    answer[i][j] -= mat[r1 - 1][c2]
                    answer[i][j] -= left_bottom

        return answer