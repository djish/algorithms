
def binary_search(arr, search, start, end):
    if(end >= 1):
        mid = start + (end-1) // 2

        # if element is the middle element. 
        if arr[mid] == search:
            return mid

        # If Element is in the first half
        if arr[mid] > search:
            return binaray_search(arr, search, start, mid-1)

        # If Element is in the next half
        if arr[mid] < search:
            return binary_search(arr, search, mid+1, end)
    else:

        return -1;

arr = [1,3,5,7,8,10,40,45,76]
search = 45

result = binary_search(arr, search, 0, len(arr) - 1)

if result == -1:
    print("element not found in array")
else:
    print("Element found in array at index ", result)