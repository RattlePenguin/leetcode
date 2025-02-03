from typing import List
import math

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # starting from (0, 0)
        # DP: SRBCFT
        # Subproblem: for 0 <= i <= m and 0 <= j <= n, let mat[i][j] be the problem of finding the minimum distance to a 0-cell
        # Recurrence
        # Subproblem can only be solved using previously computed values
        # Two passes
        # from top to bottom, left to right, taking top and left values only
        # from bottom to top, right to left, taking bottom and right values only
        # Base case: mat[i][j] == 0 ? 0 : min + 1
        # Comp: increasing i then increasing j

        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    top = mat[i - 1][j] if i > 0 else math.inf
                    left = mat[i][j - 1] if j > 0 else math.inf
                    mat[i][j] = min(top, left) + 1
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] != 0:
                    bot = mat[i + 1][j] if i < m - 1 else math.inf
                    right = mat[i][j + 1] if j < n - 1 else math.inf
                    mat[i][j] = min(mat[i][j], bot + 1, right + 1)

        return mat

def main():
    x = Solution()
    print(x.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
    print(x.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))

if __name__ == "__main__":
    main()