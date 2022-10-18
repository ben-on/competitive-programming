class Solution:
    def countAndSay(self, n: int) -> str:
        def counting(val,num):
            if num==n:
                return val
            new=[]
            cur=val[0]
            count=1
            for i in range(1,len(val)):
                if val[i]!=cur:
                    new.append(str(count)+cur)
                    count=1
                    cur=val[i]
                else:
                    count+=1
            new.append(str(count)+cur)
            return counting("".join(new),num+1)
        return counting("1",1)
            
                    
                