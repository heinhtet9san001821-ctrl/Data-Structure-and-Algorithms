class Stack:
    
    def __init__(self):
        self.arr=[]
        self.top=-1

    def is_empty(self):
        if len(self.arr)==0:
            return True
        else:
            return False

    def push(self,data):
        self.arr.append(data)    
        print(f"The data {data} is added to the stack.")
        return self.arr      

    def peek(self):
        if self.is_empty():
            print("The stack is empty!")
            return None
        return self.arr[self.top]

    def pop(self):
        if self.is_empty():
            print("The stack is still empty!")
        else:
            print(f"The data {self.peek()} is removed from the stack.")   
            self.arr.pop()
             
