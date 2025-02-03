from typing import List
import math
import random

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # naive
        # for all n points, compute dist to (0, 0) and add to array
        # sort first k
        # heap method
        # for all n points, compute dist to (0, 0) and add to heap of size k
        # to get min k, has to be a max heap
        # result is final heap
        # quickselect / quicksort
        # perform quicksort with p as the pivot
        # if p < k, we have found p elements guaranteed to be in the smallest k elements
        # if p == k, we have found the k smallest elements
        # if p > k, we can just narrow the difference

        # quicksort
        lo = 0
        hi = len(points) - 1
        while lo < hi:
            i = random.randrange(lo, hi)
            



def main():
    x = Solution()
    print(x.kClosest([[1,3],[-2,2]], 1))
    print(x.kClosest([[3,3],[5,-1],[-2,4]], 2))

if __name__ == "__main__":
    main()