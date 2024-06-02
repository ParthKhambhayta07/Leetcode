# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lengthoftree(self,root):
        if root is None:
            return 0

        left = 1 + self.lengthoftree(root.left)
        right = 1 + self.lengthoftree(root.right)

        return max(left,right)
        
    def printlevel(self,root,level):
        if root is None:
            return 

        if level == 1:
            self.l.append(root.val)  
        elif level > 1:
            self.printlevel(root.left,level - 1)
            self.printlevel(root.right,level - 1)
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        final_list = []
        
        for i in range(self.lengthoftree(root)+ 1):
            self.l = []
            self.printlevel(root,i)
            final_list.append(self.l)
            
        return final_list[1:]
        
            
    
    def __init__(self):
        global l
        global final_list 
        
        