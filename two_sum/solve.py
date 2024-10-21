from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # naive - for every int n, search n - 1 for complement
        # better - sort in nlogn time, two pointer sum
        # best - hashmap, if complement exists, then found
        hashMap = {}
        for i, item in enumerate(nums):
            if target - item in hashMap:
                return [i, hashMap[target - item]]
            else:
                hashMap[item] = i


def main():
    x = Solution()
    print(x.twoSum([2, 7, 11, 15], 9))

if __name__ == "__main__":
    main()