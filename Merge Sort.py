def mergesort(sequence):
    if(len(sequence)<2):
        return sequence
    m=len(sequence)//2
    return merge(mergesort(sequence[:m]),mergesort(sequence[m:]))
def merge(left,right):
    result=[]
    i=j=0
    while(i<len(left) and j<len(right)):
        if(left[i]<right[j]):
            result.append(left[i])
            i=i+1
        else:
            result.append(right[j])
            j=j+1
    result=result+left[i:]
    result=result+right[j:]
    return result
print("MERGE SORT")
list=[]
print("Enter number of elements:")
n=int(input())
print("Enter",n,"elements:")
for i in range(0,n):
    a=int(input())
    list.append(a)
sort=mergesort(list)
print(sort)