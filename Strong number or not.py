print("STRONG NUMBER OR NOT")
n=int(input("Enter the value of n:"))
sum=0
t=n
while(n!=0):
    d=n%10
    n=n//10
    i=1
    f=1
    while(i<=d):
        f=f*i
        i=i+1
    sum=sum+f
if(sum==t):
    print(sum,"is a strong number")
else:
    print(sum,"is not a strong number")