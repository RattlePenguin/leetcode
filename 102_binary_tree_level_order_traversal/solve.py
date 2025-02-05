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
            node = curr[0]
            if node is None:
                continue
            val = node.val
            dist = curr[1]

            if len(result) < dist + 1:
                result.append([])
            result[dist].append(val)
            
            q.appendleft([node.left, dist + 1])
            q.appendleft([node.right, dist + 1])
        return result

def main():
    x = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(x.levelOrder(root))

if __name__ == "__main__":
    main()