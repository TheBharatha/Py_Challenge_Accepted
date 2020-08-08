class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        numStr = ''
        while head:
            numStr += str(head.val)
            head = head.next
        return int(numStr,2)