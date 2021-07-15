
'''Linear Search'''
def search(arr, search):
    for i in range(0, len(arr) - 1):
        if (arr[i] == search):
            return i;
    return -1;


arr = [1, 4, 6, 10, 24]
searchTerm = 26

result = search(arr, searchTerm)

if(result == -1):
    print("Element not found in array")
else: 
    print("Element found in index ", result)