from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort nums
        # fix i
        # use two pointers to ensure unique combinations
        nums = sorted(nums)
        result = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif sum < 0:
                    j += 1
                else:
                    k -= 1
        return result


def main():
    x = Solution()
    print(x.threeSum([-1,0,1,2,-1,-4]))
    print(x.threeSum([-1,-1,1,2,-1,-4]))
    print(x.threeSum([0,1,1]))
    print(x.threeSum([0,0,0]))


if __name__ == "__main__":
    main()