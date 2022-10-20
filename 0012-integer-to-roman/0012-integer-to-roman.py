class Solution:
    def intToRoman(self, num: int) -> str:
        dic={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
        dic2={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        lst=[1000,500,100,50,10,5,1]
        i=0
        ans=[]
        while num:
            if num//lst[i]==0:
                i+=1
                continue
            if num//lst[i] < 4 :
                ans.append(dic[lst[i]]*(num//lst[i]))
            else :
                if ans:
                    temp=dic2[ans[-1][-1]]+(((num//lst[i])+1)*lst[i])
                    if temp in dic:
                        ans.pop()
                        ans.append(dic[lst[i]]+dic[temp])
                    else:
                        ans.append(dic[lst[i]]+dic[lst[i-1]])
                else :
                    ans.append(dic[lst[i]]+dic[lst[i-1]])
                    
            num=num%lst[i]
            i+=1
            
        return "".join(ans)
        