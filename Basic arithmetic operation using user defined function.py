def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def mod(x,y):
    return x%y
print("ARITHMETIC OPERATION USING FUNCTION")
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print("Addition=",add(a,b))
print("Subtraction=",sub(a,b))
print("Multiplication=",mul(a,b))
print("Quotient=",div(a,b))
print("Remainder=",mod(a,b))