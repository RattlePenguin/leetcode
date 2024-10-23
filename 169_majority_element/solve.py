from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        majority = int(len(nums) / 2)
        for elem in counter:
            if counter[elem] > majority:
                return elem

def main():
    x = Solution()
    print(x.majorityElement([3, 2, 3]))
    print(x.majorityElement([2, 2, 1, 1, 1, 2, 2]))
    print(x.majorityElement([10, 9, 9, 9, 10]))
    print(x.majorityElement([6, 5, 5]))

if __name__ == "__main__":
    main()