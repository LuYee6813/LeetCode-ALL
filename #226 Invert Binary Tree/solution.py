# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def invertTree(root):
    if root == None:
        return None
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root





class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]: 
        return invertTree(root)
        