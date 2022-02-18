def factorial(a):
    if(a==0):
        return 1
    else:
        return(a*factorial(a-1))
print("FACTORIAL USING RECURSION")
n=int(input("Enter the value of n:"))
f=factorial(n)
print("The factorial value of",n,"is",f)