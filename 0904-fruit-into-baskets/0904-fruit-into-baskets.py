class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        d={}
        res=0
        for right in range(len(fruits)):
            d[fruits[right]]=1+d.get(fruits[right],0)
            while len(d)>2:
                if d[fruits[left]]>1:
                    d[fruits[left]]-=1
                    left+=1
                else:
                    del d[fruits[left]]
                    left+=1
            res=max(res,right-left+1)
        return res
                    
        