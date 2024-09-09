def sort(arr):
    lower=0
    mid=0
    upper=len(arr)-1
    
    while mid<=upper:
        if arr[mid]==0:
            arr[mid],arr[lower]=arr[lower],arr[mid]
            lower+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        elif arr[mid]==2:
            arr[mid],arr[upper]=arr[upper],arr[mid]
            upper-=1
            mid+=1
    return arr
    
l=[]
n=int(input("Enter the range : "))
for i in range(n):
    ele=int(input())
    if ele==1 or ele==0 or ele==2:
        l.append(ele)
print(sort(l))
        