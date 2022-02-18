print("REVERSE THE NUMBER")
n=int(input("Enter the value of n:"))
rev=0
while(n!=0):
    d=n%10
    n=n//10
    rev=rev*10+d
print("Reverse of digit=",rev)