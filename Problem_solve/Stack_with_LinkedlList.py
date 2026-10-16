class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.top=None
        self._size=0

    def push(self,data):
        new_node=Node(data)
        new_node.next=self.top
        self.top=new_node

    def is_empty(self):
        return self.top is None

    def pop(self):
        if self.is_empty():
            print("The stact is empty!")

        removed_item=self.top.data
        self.top=self.top.next
        return removed_item

    def peek(self):
        return self.top.data             
