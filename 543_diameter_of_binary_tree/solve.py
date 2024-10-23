from typing import Optional

# Definiton for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getHeight(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return -1
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # None or leaf node, diameter is zero
        if root is None or (root.left is None and root.right is None):
            return 0
        
        # longest path will be max of left diameter, right diameter, and current height combinations
        myLongPath = 2 + self.getHeight(root.left) + self.getHeight(root.right)
        return max(myLongPath, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

def main():
    x = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(6)
    root.left.left.left.left = TreeNode(7)
    root.left.right.right = TreeNode(8)
    root.left.right.right.right = TreeNode(9)
    print(x.diameterOfBinaryTree(root))

if __name__ == "__main__":
    main()


# Cases
#         1
#       2   3
#     4   5
#   6       7
# 8           9
# Longest path: 8 - 9 (4)