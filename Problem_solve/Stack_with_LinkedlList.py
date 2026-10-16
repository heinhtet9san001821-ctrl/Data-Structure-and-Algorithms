class Node:#For each data , we must create each node
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:#The whole controller of the linked system 
    def __init__(self):#Constructor
        self.top=None
        self._size=0

    def push(self,data):#Adding the new item to the stack
        new_node=Node(data)
        new_node.next=self.top
        self.top=new_node

    def is_empty(self):#checking the condition of stack 
        return self.top is None

    def pop(self):#Removing the last item from the stack
        if self.is_empty():
            print("The stact is empty!")

        removed_item=self.top.data
        self.top=self.top.next
        return removed_item

    def peek(self):#Viewing the top item
        return self.top.data             
