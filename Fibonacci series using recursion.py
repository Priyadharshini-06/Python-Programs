def fibonacci(i):
        if(i==0):
              return 0
        if(i==1):
               return 1
        return(fibonacci(i-1)+fibonacci(i-2))
print("FIBONACCI SERIES USING RECURSION")
n=int(input("Enter the value of n:"))
print("The fibonacci series is:")
for i in range(0,n):
    print(fibonacci(i))