from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i, num in enumerate(nums):
            target = 0 - num
            for ans in self.twoSum(nums, i, target):
                ans.append(i)
                result.append(ans)
        return result

    def twoSum(self, nums: List[int], i: int, target: int) -> List[List[int]]:
        map = {}
        result = []
        for j, num in enumerate(nums):
            if i == j: continue
            if target - num in map:
                result.append([map[target - num], j])
            else:
                map[num] = j
        return result



def main():
    x = Solution()
    # print(x.twoSum([-1,0,1,2,-1,-4], -1, -2))
    print(x.threeSum([-1,0,1,2,-1,-4]))
    print(x.threeSum([0,1,1]))
    print(x.threeSum([0,0,0]))


if __name__ == "__main__":
    main()