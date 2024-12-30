class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        max = 0
        curr = 0
        i = 0
        while i < k:
            if s[i] in vowels:
                curr += 1
            i += 1
        max = curr
        
        while i < len(s):
            if s[i] in vowels:
                curr += 1
            if s[i - k] in vowels:
                curr -= 1
            if curr > max:
                max = curr
            i += 1
        
        return max

def main():
    x = Solution()
    print(x.maxVowels("abciiidef", 3))
    print(x.maxVowels("aeiou", 2))
    print(x.maxVowels("leetcode", 3))


if __name__ == "__main__":
    main()