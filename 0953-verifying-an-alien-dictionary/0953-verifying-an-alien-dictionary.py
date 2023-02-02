class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d={order[i]:chr(i+97) for i in range(len(order))}
        d2={chr(i+97):order[i] for i in range(len(order))}
        new=[]
        for word in words:
            temp=[]
            for ltr in word:
                temp.append(d[ltr])
            new.append(temp)
        new=["".join(i) for i in new]
        new.sort()
        new2=[]
        for wd in new:
            tmp=[]
            for lt in wd:
                tmp.append(d2[lt])
            new2.append(tmp)
        new2=["".join(j) for j in new2]
        return new2==words