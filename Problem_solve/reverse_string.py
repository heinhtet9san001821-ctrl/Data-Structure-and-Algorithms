#Our mission is to implement a function that return the reversed string 

def reverse_str(s):
    # Base case: an empty string or a single character is already reversed
    if len(s) <= 1:
        return s
    
    # Recursive case: take the last character and add it to the reversed remaining string
    return s[-1] + reverse_str(s[:-1])


user_input = input("Enter the string you want to reverse: ")
result = reverse_str(user_input)
print(result)
