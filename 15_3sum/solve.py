from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i, num in enumerate(nums):
            target = 0 - num
            map = {}
            for j, num in enumerate(nums):
                if i == j: continue
                if target - num in map:

                else:
                    map[num] = j
        result.append



def main():
    x = Solution()
    print(x.threeSum([-1,0,1,2,-1,-4]))
    print(x.threeSum([0,1,1]))
    print(x.threeSum([0,0,0]))


if __name__ == "__main__":
    main()