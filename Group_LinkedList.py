class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.oddNodes = list()
        self.evenNodes = list()
    
        
    def oddEvenList(self, head: ListNode) -> ListNode:
        nodeValue = 1
        while head:
            if nodeValue%2 == 0:
                self.evenNodes.append(head.val)
                head = head.next
            else:
                self.oddNodes.append(head.val)
                head = head.next
            nodeValue += 1
            
        self.oddNodes.extend(self.evenNodes)
        
        for nodes in self.oddNodes:
            newNode = ListNode(nodes)
            if head:
                current = head
                while current.next:
                    current = current.next
                current.next = newNode
            else:
                head = newNode
                
        return head