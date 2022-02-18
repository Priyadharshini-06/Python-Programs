print("INSERTION SORT")
list=[]
print("Enter upper limit:")
n=int(input())
print("Enter the numbers:")
for i in range(0,n):
    a=int(input())
list.append(a)
for i in range(1,n):
    data=list[i]
    j=i-1
    while((data<list[j])and(j>=0)):
        list[j+1]=list[j]
        j=j-1
    list[j+1]=data
    print("After pass=",i)
    print(list)
print("The sorted elements are:")
print(list)