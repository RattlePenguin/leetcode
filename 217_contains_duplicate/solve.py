from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for value in nums:
            if value in dict:
                return True
            else:
                dict[value] = 1
        return False

def main():
    x = Solution()
    print(x.containsDuplicate([1, 2, 3, 1]))
    print(x.containsDuplicate([1, 2, 3, 4]))
    print(x.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
    print(x.containsDuplicate([3, 3]))

if __name__ == "__main__":
    main()