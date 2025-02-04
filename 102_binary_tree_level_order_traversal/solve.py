from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# using a queue, pop elem from queue, print elem, enqueue both children
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        q = deque()
        q.appendleft([root, 0])

        while len(q) > 0:
            curr = q.pop()
            result.append([curr[0], curr[1]])
            if curr[0].left is not None:
                result.append(curr[0])
                q.appendleft([curr[0].left, curr[1] + 1])
            if curr[0].right is not None:
                result.append(curr[0].right.val)
                q.appendleft(curr[0].right)
            

def main():
    x = Solution()
    print(x.levelOrder(None))

if __name__ == "__main__":
    main()