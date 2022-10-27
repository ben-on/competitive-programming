class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        one = [(i,j) for i in range(n) for j in range(n) if img1[i][j]]
        two = [(i,j) for i in range(n) for j in range(n) if img2[i][j]]
        d = Counter((a1-b1,a2-b2) for a1,a2 in one for b1,b2 in two)
        return max(d.values() or [0])