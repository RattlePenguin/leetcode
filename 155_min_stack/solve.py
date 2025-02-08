class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        try:
            currMin = self.getMin()
        except:
            currMin = val
        self.stack.append([val, min(val, currMin)])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:

def main():
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    param_4 = obj.getMin()
    print(param_4)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
    print(param_3)
    print(param_4)



if __name__ == "__main__":
    main()