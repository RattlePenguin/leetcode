from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [1] * len(nums)
        left = 1
        for i in range(len(nums)):
            prod[i] *= left
            left *= nums[i]

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            prod[i] *= right
            right *= nums[i]

        return prod


def main():
    x = Solution()
    print(x.productExceptSelf([1,2,3,4]))
    print(x.productExceptSelf([-1,1,0,-3,3]))

if __name__ == "__main__":
    main()