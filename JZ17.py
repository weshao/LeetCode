class TreeNode():
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        result = False
        if pRoot1 is None or pRoot2 is None:
            return False
        
        if pRoot1.val == pRoot2.val:
            result = self.isSub(pRoot1, pRoot2)
        if not result:
            result = self.HasSubtree(pRoot1.left, pRoot2) | self.HasSubtree(pRoot1.right, pRoot2)

        return result

    
    
    def isSub(self, pRoot1, pRoot2):
        if pRoot1 is None:
            return False
        if pRoot2 is None:
            return True
        if pRoot1.val != pRoot2.val:
            return False
        else:
            return self.isSub(pRoot1.left, pRoot2.left) & self.isSub(pRoot1.right, pRoot2.right)
            

