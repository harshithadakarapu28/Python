#Map Function
def myfunction(x,y):
    return x+y
x = map(myfunction,("apple", "banana", "orange"),(" cheery", " grapes", " guava"))
print(list(x))
