class Solution:
    def dfs(self,target,stickers):
        if not target: 
            return 0
        if target in self.map: 
            return self.map[target]
        cnt, res = collections.Counter(target), float('inf')
        for c in stickers: 
            if c[target[0]] == 0: continue
            nxt = self.dfs(''.join([s * t for (s, t) in (cnt - c).items()]),stickers)
            if nxt != -1: res = min(res, 1 + nxt)
        self.map[target] = -1 if res == float('inf') else res
        return self.map[target]
    def minStickers(self, stickers: 'List[str]', target: 'str') -> 'int':
        stickers, self.map = [collections.Counter(s) for s in stickers if set(s) & set(target)], {}
        
        return self.dfs(target,stickers)
