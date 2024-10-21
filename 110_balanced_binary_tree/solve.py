from typing import Optional

# Definition for a binary tree node.
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
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        bf = self.getHeight(root.left) - self.getHeight(root.right)
        if bf < -1 or bf > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

def main():
    x = Solution()
    print(x.isBalanced(None))

if __name__ == "__main__":
    main()