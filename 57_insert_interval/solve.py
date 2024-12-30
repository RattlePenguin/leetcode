from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # cases
        # 1. interval is added no overlap (beginning, end)
        # 2. interval overlaps, update new interval start and end

        result = []
        length = len(intervals)
        start = newInterval[0]
        end = newInterval[1]

        i = 0
        while i < length and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1

        while i < length and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        result.append([start, end])

        while i < length:
            result.append(intervals[i])
            i += 1

        return result
            

def main():
    x = Solution()
    print(x.insert([[1,3],[6,9]], [2,5]))
    print(x.insert([[1,5]], [2,3]))
    print(x.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))

if __name__ == "__main__":
    main()