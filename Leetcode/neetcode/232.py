class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        i = self.queue.pop(0)
        return i

    def peek(self) -> int:
        fe = self.queue[0]
        return fe

    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        else:
            return False

obj = MyQueue()
obj.push(x=2)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()