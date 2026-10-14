def factorial(n):
    if n<=1: # Base case to end the recursion 
        return 1
    return n*factorial(n-1) #recursive  case to do operation

num=int(input("Enter the number you want to see in factorial : "))
result=factorial(num)
print(result)