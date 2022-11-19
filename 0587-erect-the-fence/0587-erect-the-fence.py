class Solution:
    def fslope(self,one,two):
        if one[0] == two[0]:
            return float("inf")
        return abs((two[1]-one[1])/(two[0]-one[0]))
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        trees.sort()
        # print(trees)
        n = len(trees)
        vis = {0}
        cur = 0
        while cur < n:
            great = []
            slope = -float('inf')
            for i in range(cur+1,n):
                if trees[i][1] >= trees[cur][1]:
                    if self.fslope(trees[cur],trees[i]) > slope:
                        great = [i]
                        slope = self.fslope(trees[cur],trees[i])
                    elif self.fslope(trees[cur],trees[i]) == slope:
                        great.append(i)
            if great:
                for gr in great:
                    vis.add(gr)
                cur = great[-1]
            else:
                break
        # print(vis)
        while cur < n:
            least = []
            slope = float('inf')
            for j in range(cur+1,n):
                if j not in vis:
                    if self.fslope(trees[cur],trees[j]) < slope:
                        least = [j]
                        slope = self.fslope(trees[cur],trees[j])
                    elif self.fslope(trees[cur],trees[j]) == slope:
                        least.append(j)
            if least:
                for ls in least:
                    vis.add(ls)
                cur = least[-1]
            else:
                break
        cur = 0
        # print(vis)
        while cur < n:
            least = []
            slope = -float('inf')
            for k in range(cur+1,n):
                if trees[k][1] <= trees[cur][1]:
                    if self.fslope(trees[cur],trees[k]) > slope:
                        least = [k]
                        slope = self.fslope(trees[cur],trees[k])
                    elif self.fslope(trees[cur],trees[k]) == slope:
                        least.append(k)
            if least:
                for ls in least:
                    if ls in vis:
                        return [trees[i] for i in vis]
                    vis.add(ls)
                cur = least[-1]
            else:
                break
        # print("one",cur)
        # print(vis)
        while cur < n:
            great = []
            slope = float('inf')
            for q in range(cur+1,n):
                if trees[q][1] >= trees[cur][1]:
                    if self.fslope(trees[cur],trees[q]) < slope:
                        great = [q]
                        slope = self.fslope(trees[cur],trees[q])
                    elif self.fslope(trees[cur],trees[q]) == slope:
                        great.append(q)
            if great:
                for gr in great:
                    if gr in vis:
                        return [trees[i] for i in vis]
                    vis.add(gr)
                cur = great[-1]
                
            else:
                break
        # print(vis)
        return [trees[i] for i in vis]
                    
    
            