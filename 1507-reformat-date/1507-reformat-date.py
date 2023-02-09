class Solution:
    def reformatDate(self, date: str) -> str:
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        dic = {}
        for i,m in enumerate(months):
            dic[m]= i+1
        date = date.split()
        ans = [date[-1],str(dic[date[-2]]),date[0][:-2]]
        for idx,i in enumerate(ans):
            if len(i) == 1:
                ans[idx] = '0'+ans[idx]
            
        return "-".join(ans)