from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = []
        self.inOrderTraversal(root, inorder)
        
        for i in range(1, len(inorder)):
            if inorder[i] <= inorder[i - 1]:
                return False
        return True
    
    def inOrderTraversal(self, root: Optional[TreeNode], inorder: List[int]):
        if root is None:
            return
        self.inOrderTraversal(root.left, inorder)
        inorder.append(root.val)
        self.inOrderTraversal(root.right, inorder)


def main():
    x = Solution()

if __name__ == "__main__":
    main()