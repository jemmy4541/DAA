def quicksort(arr,left,right):
    if left<right:
        parition_position=partition(arr,left,right)
        quicksort(arr, left, parition_position-1)
        quicksort(arr,parition_position+1,right)
def partition(arr,left,right):
    i=left
    j=right-1
    pivote=arr[right]
    while i<j:
        while i<right and arr[i]<pivote:
            i+=1
        while j>left and arr[j]>=pivote:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    if arr[i]>pivote:
        arr[i],arr[right]=arr[right],arr[i]
    return i
arr=[22,11,88,66,55,77,33,44]
quicksort(arr,0,len(arr)-1)
print(arr)
    
                                    
        