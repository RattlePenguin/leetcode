from typing import List
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        hashmap = {}
        myMax = -1
        for num in nums:
            digitSum = 0
            for digit in str(num):
                digitSum += int(digit)
            if digitSum in hashmap:
                myMax = max(myMax, hashmap[digitSum] + num)
                hashmap[digitSum] = max(num, hashmap[digitSum])
            else:
                hashmap[digitSum] = num

        return myMax

def main():
    x = Solution()
    print(x.maximumSum([18,43,36,13,7]))
    print(x.maximumSum([1]))
    print(x.maximumSum([1, 2]))
    print(x.maximumSum([0,0]))
    print(x.maximumSum([18,43,36,13,7,54]))
    print(x.maximumSum([9,18,27,36,45,54,63,72,81,90,111111111]))


if __name__ == "__main__":
    main()