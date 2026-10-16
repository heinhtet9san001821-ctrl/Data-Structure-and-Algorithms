class Stack:
    
    def __init__(self):# Build the constructor like this to store data in list form and to point the top and index
        self.arr=[]
        self.top=-1

    def is_empty(self):#Check for the stack is empty or not and for using in another method before operating their purpose
        if len(self.arr)==0:
            return True
        else:
            return False

    def push(self,data):#Add the item to the list
        self.arr.append(data)    
        print(f"The data {data} is added to the stack.")#Show what data is added to the stack
        return self.arr      #Return the stack after adding 

    def peek(self):#To see the item at the top of stack
        if self.is_empty():
            print("The stack is empty!")
            return None
        return self.arr[self.top]#Return what item is at the top

    def pop(self):#Remove the last item
        if self.is_empty():#Use the method we implemented above
            print("The stack is still empty!")
        else:
            print(f"The data {self.peek()} is removed from the stack.")   
            return self.arr.pop() #Return the item we removed
             
