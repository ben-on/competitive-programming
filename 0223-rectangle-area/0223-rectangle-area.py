class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        ar1 = abs(ay1-ay2)*abs(ax1-ax2)
        ar2 = abs(by1-by2)*abs(bx1-bx2)
        ans = ar1 + ar2
        xuni = min(ax2,bx2) - max(ax1,bx1)
        if xuni > 0:
            yuni = min(ay2,by2) - max(ay1,by1)
            if yuni > 0:
                ans -= xuni * yuni
        return ans