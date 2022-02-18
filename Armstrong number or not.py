print("ARMSTRONG NUMBER OR NOT")
n=int(input("Enter the value of n:"))
arms=0
t=n
while(n!=0):
    d=n%10
    n=n//10
    arms=arms+d*d*d
if(arms==t):
    print(arms,"is an armstrong number")
else:
    print(arms,"is not an armstrong number")