# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.count = 0
        def dfs(root,max_value):
            if not root:
                return None
            if root.val >=  max_value:
                self.count+=1
            max_value = max(max_value,root.val)
            
            dfs(root.left,max_value)
            dfs(root.right,max_value)
        dfs(root,root.val)
        return self.count