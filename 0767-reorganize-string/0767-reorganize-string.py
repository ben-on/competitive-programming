class Solution:
    def reorganizeString(self, s: str) -> str:
        d = Counter(s)
        # print(list(d.values()))
        if max(list(d.values())) > ceil(len(s)/2):
            return ""
        hp = [[-d[i],i] for i in d]
        heapify(hp)
        ans = ''
        while hp:
            idx1,char1= heappop(hp)
            ans+=char1
            idx1+=1
            
            if hp:
                idx2,char2= heappop(hp)
                idx2+=1
                ans+=char2
                if idx2<0:
                    heappush(hp,[idx2,char2])
            if idx1<0:
                heappush(hp,[idx1,char1])
        return ans
            
            
            
        