def change_upper(func):
    def inner():
        return func().upper()
    return inner


@change_upper
def show_name():
    return "hein htet san"

def show_name1():
    return "kaung htet naing"

@change_upper
def show_name2():
    return "min htet kyaw"

def show_name3():
    return "soe paing aung"

def show_name4():
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