from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine) # O(m)
        for char in ransomNote: # O(n)
            counter[char] -= 1
            if counter[char] < 0:
                return False

        return True


def main():
    x = Solution()
    print(x.canConstruct("a", "b"))
    print(x.canConstruct("aa", "ab"))
    print(x.canConstruct("aa", "aab"))

if __name__ == "__main__":
    main()