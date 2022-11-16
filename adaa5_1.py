def quicksort(arr, low, high):
    if low<high:
        pi=partition(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)
def partition(arr, low, high):
    pivot=arr[high]
    
    i=low-1
    for j in range(low, high):
        if array[j]<=pivot:
            i=i+1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i+1],arr[high])=(arr[high], arr[i+1])
    return i+1
        
data = [1, 7, 4, 1, 10, 9, -2]
size = len(data)
quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)