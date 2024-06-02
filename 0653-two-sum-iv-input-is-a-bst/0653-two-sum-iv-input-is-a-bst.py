# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
         d = set()
    
         def find(root):
            if root:
                if root.val in d: return True
                d.add(k-root.val)
                return find(root.left) or find(root.right)
            return False
    
         return find(root)
            
            
            