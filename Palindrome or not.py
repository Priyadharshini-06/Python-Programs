print("PALINDROME OR NOT")
n=int(input("Enter the value of n:"))
rev=0
t=n
while(n!=0):
    d=n%10
    n=n//10
    rev=rev*10+d
if(rev==t):
    print(rev,"is a palindrome")
else:
    print(rev,"is not a palindrome")