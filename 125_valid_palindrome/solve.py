import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = re.sub('[^a-zA-Z0-9]', '', s.lower())
        
        i = 0
        j = len(string) - 1
        while i <= j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        
        return True

def main():
    x = Solution()
    print(x.isPalindrome("rac ec ar"))
    print(x.isPalindrome("A man, a plan, a canal: Panama"))
    print(x.isPalindrome(""))
    print(x.isPalindrome(" "))
    print(x.isPalindrome("    "))
    print(x.isPalindrome("rrrrrraaa"))


if __name__ == "__main__":
    main()