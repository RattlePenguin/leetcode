from typing import List
import numpy as np

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # starting from (0, 0)
        # DP: increasing i, where i is number of blocks away from (0, 0)
        # base case i = 0, if (0, 0) is 0, then put 0, otherwise leave empty

        dp = [[] for _ in range(len(mat))]
        for i, row in enumerate(mat):
            for j, col in enumerate(mat[i]):
                if col == 0:
                    dp[i].append(0)
                else:
                    dp[i].append(np.inf)

        

def main():
    x = Solution()
    print(x.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
    print(x.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))

if __name__ == "__main__":
    main()