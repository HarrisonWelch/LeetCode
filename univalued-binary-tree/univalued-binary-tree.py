# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        return self.isUnivalTreeRecursive(root, root.val)
    
    def isUnivalTreeRecursive(self, root: Optional[TreeNode], val: int) -> bool:
        if root is None:
            return True
        
        return \
            self.isUnivalTreeRecursive(root.left, val) \
            and val == root.val \
            and self.isUnivalTreeRecursive(root.right, val)
