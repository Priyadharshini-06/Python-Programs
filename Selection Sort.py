print("SELECTION SORT")
list=[]
print("Enter upper limit:")
n=int(input())
print("Enter the numbers:")
for i in range(0,n):
    a=int(input())
    list.append(a)
for i in range(0,n-1):
    min=i
    for j in range(i+1,n):
        min=i
        for j in range(i+1,n):
            if(list[min]>list[j]):
                min=j
        if(i!=min):
            k=list[i]
            list[i]=list[min]
            list[min]=k
        print("After pass=",i+1)
        print(list)
        print("The sorted elements are:")
        print(list)