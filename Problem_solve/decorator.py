def change_upper(func):# Implement the function first to use later as a @change_upper
    def inner():
        return func().upper()
    return inner


@change_upper#Use the above function to change or operate the below function without changing the source code
def show_name():#Now, this function is tagged with @change_upper, so the output will be modified due to the tag,@change_upper
    return "hein htet san"

def show_name1():#untagged function
    return "kaung htet naing"

@change_upper
def show_name2():#tagged function 
    return "min htet kyaw"

def show_name3():#untagged
    return "soe paing aung"

def show_name4():#untagged
    return "khink kyi myint"



name=show_name()
name1=show_name1()
name2=show_name2()
name3=show_name3()
name4=show_name4()
print(name)    
print(name1)
print(name2)
print(name3)
print(name4)