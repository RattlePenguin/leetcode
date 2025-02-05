from typing import List
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(token)
                continue
            if len(stack) < 2:
                print("error")
                return 0
            second = stack.pop()
            first = stack.pop()
            if token == "+":
                res = int(first) + int(second)
                stack.append(str(res))
            if token == "-":
                res = int(first) - int(second)
                stack.append(str(res))
            if token == "*":
                res = int(first) * int(second)
                stack.append(str(res))
            if token == "/":
                res = int(first) // int(second)
                res = math.trunc(res)
                stack.append(str(res))
        return int(stack[0])

def main():
    x = Solution()
    print(x.evalRPN(["2","1","+","3","*"]))


if __name__ == "__main__":
    main()