from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])

        i = 1
        for num in nums[1:]:
            if dp[i - 1] > 0:
                dp.append(dp[i - 1] + num)
            else:
                dp.append(num)
            i += 1

        return max(dp)

def main():
    x = Solution()
    print(x.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(x.maxSubArray([1]))
    print(x.maxSubArray([5, 4, -1, 7, 8]))
    print(x.maxSubArray([-1]))
    print(x.maxSubArray([-2, 1]))

if __name__ == "__main__":
    main()