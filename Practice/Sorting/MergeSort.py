def merge(arr,l,mid,r):
    temp=[]
    i=l
    j=mid+1
    while i<=mid and j<=r:
        if arr[i]<arr[j]:
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j+=1
        
    while i<=mid:
        temp.append(arr[i])
        i+=1
    while j<=r:
        temp.append(arr[j])
        j+=1
    for k,val in enumerate(temp):
        arr[l+k]=val

def mergeSort(arr: [int], l: int, r: int):
    print(l,r)
    if l>=r:
        return
    mid=((l+r)//2)
    mergeSort(arr,l,mid)
    mergeSort(arr,mid+1,r)
    merge(arr,l,mid,r)

