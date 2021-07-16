

def interpolation_search(arr, search, low, high):

    if ( low <= high and search >= arr[low] and search <= arr[high]):

        pos = low + ((high - low) // (arr[high] - arr[low]) * search - arr[low])

        if arr[pos] == search:
            return pos
        
        if arr[pos] < search:
            return interpolation_search(arr, search, low, pos+1)

        if arr[pos] > search:
            return interpolation_search(arr, search, pos -1, high)

    return -1


arr = [10, 12, 13, 16, 18, 19, 20,
       21, 22, 23, 24, 33, 35, 42, 47]
search = 18

result = interpolation_search(arr, search, 0, len(arr) - 1)

if result == -1:
    print("Element not found in array")
else:
    print("element found at index", result)