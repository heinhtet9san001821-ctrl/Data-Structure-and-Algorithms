#String palindrome checking 

sr=input("Enter the string you want to check: ")

def check(st):
    if len(st)<=1:
        return True
    if st[0]!=st[-1]:
        return False
    return check(st[1:-1])

if check(sr):
    print(f"The given string {sr} is a palindrome.")
else:
    print(f"The given string {sr} is not a palindrome.")    