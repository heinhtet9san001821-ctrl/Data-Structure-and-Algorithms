sr=input("Enter the string you want to check: ")

def check(st):
    l=0 #To point the first index of string
    r=len(sr)-1# To point the last index of string
    while r > l:#To control the loop by checking whether the position is in the mid or not! 
       if st[l] == st[r]:
           l+=1# To move a position from 0 index to mid
           r-=1# To move a position from -1 index to mid
       else:
           return False
       return True



if check(sr):
    print(f"The given string {sr} is a palindrome.")
else:
    print(f"The given string {sr} is not a palindrome.")    