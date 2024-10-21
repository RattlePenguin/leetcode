class Solution:
    def isValid(self, s: str) -> bool:
        # Make a stack, if closing comes before opening then invalid...
        stack = []
        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            else:
                try:
                    opener = stack.pop()
                except:
                    opener = None
                
                if opener is None or opener + char not in ["()", "{}", "[]"]:
                    return False
        
        if len(stack) != 0:
            return False
        return True


def main():
    x = Solution()
    print(x.isValid("(){}[]"))
    print(x.isValid("({[]})"))
    print(x.isValid("([{])}"))
    print(x.isValid("}({[]})"))

if __name__ == "__main__":
    main()