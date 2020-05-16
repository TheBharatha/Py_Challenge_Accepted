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
'''
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        lo, hi = head, head.next
        while hi and hi.next: 
            lo.next, hi.next.next, hi.next = hi.next, lo.next, hi.next.next
            lo, hi = lo.next, hi.next
        return head 
'''