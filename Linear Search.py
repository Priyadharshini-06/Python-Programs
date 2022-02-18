print("LINEAR SEARCH")
list=[]
print("Enter upper limit:")
n=int(input())
print("Enter the numbers:")
for i in range(0,n):
        a=int(input())
        list.append(a)
search=int(input("Enter the elements to be searched:"))
i=flag=0
while(i<len(list)):
      if list[i]==search:
            flag=1
            break
      i=i+1
if(flag==1):
    print("Element found at position:",i+1)
else:
    print("Element not found in a list")