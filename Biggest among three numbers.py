print("BIGGEST AMONG THREE NUMBERS")
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
if(a>b) and (a>c):
    big=a
elif(b>a) and (b>c):
     big=b
else:
     big=c
print("The biggest number is ",big)