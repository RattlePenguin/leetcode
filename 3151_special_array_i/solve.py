from typing import List
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        oddNext = False
        if nums[0] % 2 == 0:
            oddNext = True

        for i in range(1, len(nums)):
            if oddNext != bool(nums[i] % 2 == 1):
                return False
            oddNext = not oddNext
        return True
    
def main():
    x = Solution()

if __name__ == "__main__":
    main()
