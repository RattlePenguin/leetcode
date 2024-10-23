# The isBadVersion API is already defined for you.

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # binary search
        lo = 1
        hi = n
        while lo <= hi:
            i = int((hi - lo)/2 + lo)
            print(i)
            if isBadVersion(i):
                lastBad = i
                hi = i - 1
            else:
                lo = i + 1
        
        return lastBad

def main():
    x = Solution()
    print(x.firstBadVersion(3))
    print(x.firstBadVersion(5))
    print(x.firstBadVersion(9))
    print(x.firstBadVersion(10))
    print(x.firstBadVersion(50))

def isBadVersion(version: int) -> bool:
        if version < 2:
            return False
        else:
            return True

if __name__ == "__main__":
    main()