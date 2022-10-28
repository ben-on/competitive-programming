class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs :
            b="".join(sorted(i))
            if b in d :
                d[b].append(i)
            else :
                d[b]=[i]
        return list(d.values())
    
            