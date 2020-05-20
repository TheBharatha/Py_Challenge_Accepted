# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.kSmall = 0
        self.count = 0
    
    def traversal(self, root, k):
        if root == None:
            return
        
        self.traversal(root.left, k)
        self.count += 1
        if self.count == k:
            self.kSmall = root.val
            return
        self.traversal(root.right, k)
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.traversal(root, k)
        return self.kSmall