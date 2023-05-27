def rev(arr, i , j):
    if (i==j):
        return;
    rev(arr, i+1, j-1)
    arr[i], arr[j] = arr[j], arr[i]
    print(arr)

    
arr = [1,2,3,4,5]
print("before sorting: ",arr)
rev(arr, 0, len(arr)-1)
print("after sorting: ", arr)
