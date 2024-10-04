class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stk = []

        for ast in asteroids:
            if ast > 0:
                stk.append(ast)
            else:
                while stk and stk[-1] > 0 and abs(ast) >= stk[-1]:
                    val = stk.pop()
                    if abs(ast) == val:
                        break
                else:
                    if not stk or stk[-1] < 0:
                        stk.append(ast)
        
        return stk
        