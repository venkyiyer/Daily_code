class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        i = self.stack.pop()
        return i

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        else:
            return False

obj = MyStack()
obj.push(x=2)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()