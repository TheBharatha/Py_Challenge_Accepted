class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
# A unique solution; No temp variable to store the current node as previous node for comparision
    def removeDuplicates(self,head):
        cur_item = head
        while cur_item.next != None:
            next_item = cur_item.next
            if cur_item.data == next_item.data:
                cur_item.next = next_item.next
                next_item = None
            else:
                cur_item = cur_item.next
        return(head)
        

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 
