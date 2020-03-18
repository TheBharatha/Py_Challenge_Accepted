class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary = ''
        decimal, i = 0, 0
        while head:
            binary = binary + str(head.val)
            head = head.next
        binary = int(binary)
        while binary != 0:
            dec = binary % 10
            decimal = decimal + dec * pow(2,i)
            binary = binary//10
            i += 1
        return(decimal)
