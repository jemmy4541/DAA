import random 

def quicksort(arr, low, high):
    if low<high:
        pi=pivotran(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)
        
def pivotran(arr, low, high):
    randpvt=random.randrange(low, high)
    
    arr[low], arr[randpvt]=arr[randpvt], arr[low]
    
    return partition(arr, low, high)

def partition(arr, low, high):
    pivot=low
    
    i=low+1
    for j in range(low+1, high+1):
        if arr[j]<=arr[pivot]:
            arr[i],arr[j]=arr[j],arr[i]
            i=i+1
    arr[pivot], arr[i-1]=arr[i-1],arr[pivot]
    pivot=i-1
    return(pivot)

if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5]
    quicksort(array, 0, len(array) - 1)
    print(array)