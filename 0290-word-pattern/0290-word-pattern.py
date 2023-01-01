class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wds = s.split()
        pt = list(pattern)
        dic = {}
        dic2 = {}
        if len(pt) != len(wds):
            return False
        for i in range(len(pt)):
            if pt[i] in dic:
                if dic[pt[i]] != wds[i]:
                    return False
            elif wds[i] in dic2:
                return False
            else:
                dic[pt[i]] = wds[i]
                dic2[wds[i]] = pt[i]
        return True


                
                    

