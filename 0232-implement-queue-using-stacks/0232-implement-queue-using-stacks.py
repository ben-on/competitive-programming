class MyQueue:

    def __init__(self):
        self.qu=deque([])

    def push(self, x: int) -> None:
        self.qu.append(x)

    def pop(self) -> int:
        return self.qu.popleft()

    def peek(self) -> int:
        return self.qu[0]

    def empty(self) -> bool:
        return not self.qu


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()