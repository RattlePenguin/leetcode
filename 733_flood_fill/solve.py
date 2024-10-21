from typing import List

class Solution:
    def dfs(self, rows: int, cols: int, image: List[List[int]], visited: List[List[int]], sr: int, sc: int, color: int, ocolor: int):
        if sr < 0 or sr >= rows or sc < 0 or sc >= cols or visited[sr][sc] != 0 or image[sr][sc] != ocolor:
            return
        else:
            image[sr][sc] = color
            visited[sr][sc] = 1
        
        self.dfs(rows, cols, image, visited, sr + 1, sc, color, ocolor)
        self.dfs(rows, cols, image, visited, sr - 1, sc, color, ocolor)
        self.dfs(rows, cols, image, visited, sr, sc + 1, color, ocolor)
        self.dfs(rows, cols, image, visited, sr, sc - 1, color, ocolor)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = (len(image), len(image[0]))
        visited = [[0 for i in range(cols)] for j in range(rows)]
        ocolor = image[sr][sc]
        self.dfs(rows, cols, image, visited, sr, sc, color, ocolor)
        return image

def main():
    x = Solution()
    print(x.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
    print(x.floodFill([[0,0,0],[0,0,0]], 0, 0, 0))

if __name__ == "__main__":
    main()
