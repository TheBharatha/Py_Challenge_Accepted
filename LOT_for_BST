class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        if root is None:
            return
        bst = Queue()
        bst.add(root)
        move = ""
        while len(bst) > 0:
            move += str(bst.peek()) + ' '
            item = bst.retrive()
            if item.left:
                bst.add(item.left)
            if item.right:
                bst.add(item.right)
        print(move)

class Queue():
    def __init__(self):
        self.items = []
    def add(self,element):
        self.items.insert(0, element)
    def retrive(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        if not self.is_empty():
            return self.items[-1].data
    def __len__(self):
        return self.size()
    def size(self):
        return len(self.items)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
