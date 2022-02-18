print("SWAPPING OF TWO NUMBERS WITHOUT USING THIRD VARIABLE")
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print("Before Swapping a=",a,"b=",b)
a=a+b
b=a-b
a=a-b
print("After Swapping a=",a,"b=",b)