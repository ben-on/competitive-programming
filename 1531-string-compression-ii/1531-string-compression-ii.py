class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n=len(s)
        @cache
        def check(i,pv,l,k):
            if k<0:
                return 101
            if i>n:
                return 0
            dt=check(i+1,pv,l,k-1)
            kp=0
            if i<n:
                if (ord(s[i])-ord('a'))==pv:
                    if l==1 or l==9 or l==99:
                        kp+=1
                    kp=kp+check(i+1,pv,l+1,k)
                else:
                    kp=1+check(i+1,ord(s[i])-ord('a'),1,k);
            return min(dt,kp);
        return check(0,26,0,k)