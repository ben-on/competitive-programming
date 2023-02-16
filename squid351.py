class Solution:
    def romanToInt(self, s: str) -> int:
        myint=0
        lst=[i for i in s]
        dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(len(lst)):
            if lst[i]=='' :
                continue
            elif i==len(lst)-1:
                myint += dic[lst[i]]
            elif dic[lst[i]] >= dic[lst[i+1]]:
                myint += dic[lst[i]]
            elif dic[lst[i]] < dic[lst[i+1]] :
                myint += dic[lst[i+1]]-dic[lst[i]]
                lst[i+1]=''
        return myint
