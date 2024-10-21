class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        myDict = {}
        for i in s:
            myDict[i] = 1 + myDict.get(i, 0)

        for i in t:
            myDict[i] = myDict.get(i, 0) - 1

        for item in myDict.values():
            if item != 0:
                return False
        
        return True

def main():
    x = Solution()
    print(x.isAnagram("anagram", "nagaram"))
    print(x.isAnagram("rat", "car"))

if __name__ == "__main__":
    main()