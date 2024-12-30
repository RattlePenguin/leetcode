from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # cases
        # 1. interval is added no overlap (beginning, end)
        # 2. interval overlaps, update new interval start and end

        result = []
        start = newInterval[0]
        end = newInterval[1]

        toAdd = None
        for i, interval in enumerate(intervals):
            if interval[1] < start:
                result.append(interval)
            elif interval[0] > end:
                if toAdd is not None:
                    result.append(toAdd)
                    toAdd = None
                result.append(interval)
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])
                toAdd = [start, end]
        
        return result
            

def main():
    x = Solution()
    print(x.insert([[1,3],[6,9]], [2,5]))
    print(x.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))

if __name__ == "__main__":
    main()