print("PRIME NUMBER OR NOT")
n=int(input("Enter the value of n:"))
i=2
c=0
while(i<=n/2):
    if(n%i==0):
        c=1
        break
    i=i+1
if(c==0):
    print(n,"is a prime number")
else:
   print(n,"is not a prime number")
    
