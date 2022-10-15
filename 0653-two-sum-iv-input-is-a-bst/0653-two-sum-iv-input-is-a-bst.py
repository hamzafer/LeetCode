# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self,root,l):
        if root == None:
            return 
        self.inorderTraversal(root.left,l)
        l.append(root.val)
        self.inorderTraversal(root.right,l)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        res=[]
        self.inorderTraversal(root, res)
        for i, v in enumerate(res):
            target = k - v
            if target in res and res.index(target) != i:
                return True
        return False
