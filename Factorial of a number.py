print("FACTORIAL OF A NUMBER")
n=int(input("Enter the value of n:"))
i=1
fact=1
while(i<=n):
    fact=fact*i
    i=i+1
print("The factorial of",n,"is=",fact)