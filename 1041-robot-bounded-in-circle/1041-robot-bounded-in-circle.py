class Solution:
    def isRobotBounded(self, inst: str) -> bool:
        x,y = 0,0
        drxn_x,drxn_y = 0,1
        for i in inst:
            if i == 'G':
                x,y = x+ drxn_x, y + drxn_y
            elif i =='L':
                drxn_x, drxn_y= -1*drxn_y,drxn_x
            else:
                drxn_x, drxn_y = drxn_y, -1*drxn_x
        return (x,y) == (0,0) or (drxn_x,drxn_y) != (0,1)
    
            