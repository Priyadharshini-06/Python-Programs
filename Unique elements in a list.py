print("UNIQUE ELEMENTS IN A LIST")
list=[]
print("Enter Upper limit:")
n=int(input())
print("Enter the numbers:")
for i in range(0,n):
        a=int(input())
        list.append(a)
print("The unique elements are:")
for i in range(0,n):
        s=1
        for j in range(0,n):
            if(list[i]==list[j])and(i!=j):
                s=0
            if(s==1):
                print(list[i])
                