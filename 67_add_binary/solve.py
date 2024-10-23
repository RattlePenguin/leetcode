class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # at each digit, % and / to get 1 or 0
        # if 1 + 1, carry over
        # else digit will equal sum
        
        short = min(len(a), len(b))
        
        c = ""
        for pos in range(1, short + 1):
            print(pos)
            if a[-pos] == "1" and b[-pos] == "1":
                c = "1" + c
                c += "0"
            elif a[-pos] == "0" and b[-pos] == "0":
                c += "0"
            else:
                c += "1"
        
        # prepend longer
        a = a[:len(a) - short]
        b = b[:len(b) - short]
        c = a + b + c
    
        return c

def main():
    x = Solution()
    print(x.addBinary("11", "1"))
    print(x.addBinary("1010", "1011"))
    print(x.addBinary("0", "1"))
    print(x.addBinary("10", "1"))
    print(x.addBinary("10000", "1"))
    print(x.addBinary("100", "101"))
    print(x.addBinary("1111", "1011"))

if __name__ == "__main__":
    main()