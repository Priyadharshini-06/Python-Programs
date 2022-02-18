print("SUM OF DIGITS OF A NUMBER")
n=int(input("Enter the value of n:"))
sum=0
while(n!=0):
    d=n%10
    n=n/10
    sum=sum+d
print("Sum of digits=",sum)