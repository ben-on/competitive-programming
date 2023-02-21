class Solution:
    def shortestPathAllKeys(self, grid: [str]) -> int:
        h, w = len(grid), len(grid[0])
        n_keys = 0
        bi, bj = 0, 0
        for i in range(h):
            for j in range(w):
                c = grid[i][j]
                if c in 'abcdef':
                    n_keys += 1
                if c == '@':
                    bi, bj = i, j
        q = deque()
        q += [[bi, bj, '@.abcdef', 0, 0]]
        vis = set()
        while q:
            i, j, key, steps, vis_keys = q.pop()

            c = grid[i][j]
            if c in 'abcdef' and c.upper() not in key:
                key += c.upper()
                vis_keys += 1
            if vis_keys == n_keys:
                return steps
            for di, dj in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
                ni, nj = i + di, j + dj
                if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] in key:
                    if (ni, nj, key) not in vis:
                        vis.add((ni, nj, key))
                        q.appendleft([ni, nj, key, steps + 1, vis_keys])
        return -1
