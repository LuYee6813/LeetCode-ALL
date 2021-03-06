# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def dfs(root, depth, result):
    if root == None:
        return
    if depth == len(result):
        result.append([])
        
    result[depth].append(root.val)
    
    dfs(root.left, depth+1, result)
    dfs(root.right, depth+1, result)
    
    
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        dfs(root,0,result)
        result.reverse()
        return result