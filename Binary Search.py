print("BINARY SEARCH")
list=[]
print("Enter upper limit:")
n=int(input())
print("Enter the numbers in ascending order:")
for i in range(0,n):
    a=int(input())
    list.append(a)
search=int(input("Enter the element to be searched:"))
n=len(list)
flag=0
first=0
last=n-1
while first<=last:
    middle=int((first+last)/2)
    if search<list[middle]:
        last=middle-1
    elif search>list[middle]:
        first=middle+1
    else:
        flag=1
        break
if(flag==1):
    print("Element found at position:",middle+1)
else:
     print("Element not found at position in a list")
    