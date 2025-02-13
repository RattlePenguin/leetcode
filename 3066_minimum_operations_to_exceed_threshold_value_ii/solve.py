from typing import List
import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums) # O(n)

        minOps = 0
        while True: # O(n)
            x = heapq.heappop(nums)
            if x >= k:
                break
            y = heapq.heappop(nums)

            heapq.heappush(nums, min(x, y) * 2 + max(x, y)) # O(logn)
            minOps += 1
        return minOps

def main():
    x = Solution()
    print(x.minOperations([2,11,10,1,3], 10))
    print(x.minOperations([1,1,2,4,9], 20))


if __name__ == "__main__":
    main()
