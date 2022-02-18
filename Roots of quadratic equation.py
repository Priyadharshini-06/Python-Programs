import math
print("ROOTS OF QUADRATIC EQUATION")
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
d=(b*b)-(4*a*c)
if(d==0):
    print("Roots are real and equal")
    r1=r2=(-b)/(2*a)
    print("The roots are:",r1,r2)
elif(d>0):
    print("Roots are real and unequal");
    r1=(-b+(math.sqrt(d)))/(2*a);
    r2=(-b-(math.sqrt(d)))/(2*a);
    print("The roots are:",r1,r2);
else:
    print("The roots are imaginary")
    r1=(-b)/(2*a)
    r2=(math.sqrt(-d))/(2*a)
    print("The roots are:",r1,"+i",r2,"and",r1,"-i",r2)