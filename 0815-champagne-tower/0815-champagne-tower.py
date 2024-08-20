class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [poured]
        for r in range(query_row):
            new = [max(0, (i - 1)/2 ) for i in row]
            new.append(0)
            n = len(new)
            for i in range(1,n):
                new[i] += max(0, (row[i-1] - 1)/2 )
            
            row = new
            print(row)
        
        return min(1,row[query_glass])
            
        


                