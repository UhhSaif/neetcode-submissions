class MinStack:

    def __init__(self):
        # normal stack
        self.stack = []

        # min stack
        self.mins = []

    def push(self, val: int) -> None:
        # add to normal stack
        self.stack.append(val)

        # set val to min
        val = min(val, self.mins[-1] if self.mins else val)
        
        self.mins.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
        
