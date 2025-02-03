from typing import List
import math
import random

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # quickselect / quicksort
        # perform quicksort with p as the pivot
        # if p < k, we have found p elements guaranteed to be in the smallest k elements
        # if p == k, we have found the k smallest elements
        # if p > k, we can just narrow the difference
        # partitioning:
        # random pivot, make it 0

        dist = lambda p : p[0]**2 + p[1]**2
        
        def partition(lo: int, hi: int) -> int:
            rand = random.randint(lo, hi)
            pDist = dist(points[rand])
            # swap last and pivot
            points[rand], points[hi] = points[hi], points[rand]
            
            i = lo
            for j in range(lo, hi + 1):
                if dist(points[i]) <= pDist:
                    # swap i and j
                    points[i], points[j] = points[j], points[i]
                    i += 1
            return i - 1

        lo, hi, p = 0, len(points) - 1, len(points)
        while p != k:
            p = partition(lo, hi)
            if p < k:
                lo = p + 1
            else:
                hi = p - 1
        return points[:k]


def main():
    x = Solution()
    print(x.kClosest([[1,3],[-2,2]], 1))
    print(x.kClosest([[3,3],[5,-1],[-2,4]], 2))
    print(x.kClosest([[68,97],[34,-84],[60,100],[2,31],[-27,-38],[-73,-74],[-55,-39],[62,91],[62,92],[-57,-67]], 5))

if __name__ == "__main__":
    main()