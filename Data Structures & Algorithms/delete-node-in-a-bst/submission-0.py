# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, key=0, left=None, right=None):
#         self.key = key
#         self.left = left
#         self.right = right
class Solution:
    def minkeynode(self,root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minkeynode=self.minkeynode(root.right)
                root.val = minkeynode.val
                root.right = self.deleteNode(root.right,minkeynode.val)
        return root