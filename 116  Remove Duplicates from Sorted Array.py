def rem(arr):
    n=len(arr)
    if n <=1:
        return n
    uni=set(arr)
    arr[:n]=uni
    return len(uni)

arr=[1,1,2]
n=rem(arr)
for i in range(n):
    print(arr[i],end= " ")
    