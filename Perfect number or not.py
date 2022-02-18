print("PERFECT NUMBER OR NOT")
n=int(input("Enter the value of n:"))
s=0
i=1
while(i<n):
    if(n%i==0):
        s=s+i
    i=i+1
if(s==n):
    print(n,"is a perfect number")
else:
    print(n,"is not a perfect number")
    
