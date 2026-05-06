class MinStack:

    def __init__(self):
        self.minStack = []
        self.mainStack = []

    def push(self, val: int) -> None:
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        self.mainStack.append(val)

    def pop(self) -> None:
        if self.minStack[-1] == self.mainStack[-1]:
            self.minStack.pop()
        self.mainStack.pop()

    def top(self) -> int:
        return self.mainStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
