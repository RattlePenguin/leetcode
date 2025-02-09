from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        numGood = 0
        cache = {}
        for i, num in enumerate(nums):
            key = num - i
            numGood += cache.get(key, 0)
            cache[key] = cache.get(key, 0) + 1

        return (len(nums) * (len(nums) - 1)) // 2 - numGood

def main():
    x = Solution()
    print(x.countBadPairs([4,1,3,3]))
    print(x.countBadPairs([1,2,3,4,5]))
    print(x.countBadPairs([5,4,3,2,1]))
    print(x.countBadPairs([5,1,2,3,2]))

if __name__ == "__main__":
    main()