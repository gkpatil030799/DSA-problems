# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        p=root
        q=subRoot
        def dfs(p,q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return dfs(p.left,q.left) and dfs(p.right,q.right)
            return False

        def subroot(p,q):
            if not q:
                return True
            if not p:
                return False

            if dfs(p,q):
                return True
            
            return subroot(p.left,q) or subroot(p.right,q)
        return subroot(p,q)
        