class Solution:
    def checkValidString(self, s: str) -> bool:
        stk = []
        excuse = 0
        for i in s:
            if i == ')':
                
                if excuse:
                    excuse-=1
                else:
                    if stk:
                        stk.pop()
                    else:
                        return False
                     
            elif i == "(":
                stk.append(i)
            else:
                excuse+=1
        return  len(stk)<=excuse
                
