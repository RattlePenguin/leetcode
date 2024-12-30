class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = ""
        carry = 0
        ai = len(a) - 1
        bi = len(b) - 1

        while ai >= 0 or bi >= 0 or carry > 0:
            if ai >= 0:
                carry += int(a[ai])
            if bi >= 0:
                carry += int(b[bi])
            
            sum = str(carry % 2) + sum
            carry //= 2
            ai -= 1
            bi -= 1
        
        return sum

def main():
    x = Solution()
    print(x.addBinary("11", "1"))
    print(x.addBinary("1010", "1011"))
    print(x.addBinary("0", "1"))
    print(x.addBinary("10", "1"))
    print(x.addBinary("10000", "1"))
    print(x.addBinary("100", "101"))
    print(x.addBinary("1111", "1011"))
    print(x.addBinary("10100000100100110110010000010101111011011001101110111111111101000000101111001110", "10100000100100110110010000010101111011011001101110111111111101000000101111001110"))

if __name__ == "__main__":
    main()