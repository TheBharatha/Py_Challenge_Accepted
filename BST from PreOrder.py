from itertools import takewhile
from itertools import dropwhile
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder):
        if preorder:
            return TreeNode(preorder[0],
                           self.bstFromPreorder(tuple(takewhile(lambda x:x<preorder[0], preorder[1:]))),
                           self.bstFromPreorder(tuple(dropwhile(lambda x:x<preorder[0], preorder[1:]))))