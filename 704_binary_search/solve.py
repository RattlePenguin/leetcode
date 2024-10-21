from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            i = int(hi - lo / 2 + lo)
            if nums[i] < target:
                lo = i + 1
            elif nums[i] > target:
                hi = i - 1
            else:
                return i
        
        return -1

def main():
    x = Solution()
    print(x.search([-1,0,3,5,9,12], 9))
    print(x.search([-1,0,3,5,9,12], 2))

if __name__ == "__main__":
    main()