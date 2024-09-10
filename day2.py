def missing_ele(arr):
    l=len(arr)
    if len(arr)==1:
            if arr[0]==1:
                return 2
            elif arr[0]==2:
                return 1
    for i in range(1,l+1):
        if i not in arr:
            return i


n=int(input("Enter the range : "))
if n>10000000:
    n=int(input("Enter valid range : "))
arr=[]
for i in range(1,n):
    ele=int(input())
    arr.append(ele)
print("Missing value : " ,missing_ele(arr))