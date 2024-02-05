class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_needs = [(target - position[i]) / speed[i] for i in range(len(position))]
        time_with_pos = sorted(list(zip(position, time_needs)))
        stack = []

        for i in range(len(position)):
            while stack and stack[-1] <= time_with_pos[i][1]:
                stack.pop()
            stack.append(time_with_pos[i][1])
        
        return len(stack)