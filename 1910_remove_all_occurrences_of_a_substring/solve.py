import re
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        curr = s
        prev = s
        curr = re.sub(part, "", curr, 1)
        while curr != prev:
            prev = curr
            curr = re.sub(part, "", curr, 1)
    
        return curr
        

def main():
    x = Solution()
    # print(x.removeOccurrences("daabcbaabcbc", "abc"))
    # print(x.removeOccurrences("axxxxyyyyb", "xy"))
    print(x.removeOccurrences("aabababa", "aba"))

if __name__ == "__main__":
    main()