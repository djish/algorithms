import math

def jump_search(arr, search):

    arr_len = len(arr)
    jump_blocks = math.sqrt(arr_len)

    prev = 0
    while arr[int(min(jump_blocks, arr_len) -1)] < search:
        prev = jump_blocks
        jump_blocks += math.sqrt(arr_len)
        if prev >= arr_len:
            return -1

    while arr[int(prev)] < search:
        prev += 1

        if prev == min(jump_blocks, arr_len):
            return -1

    if arr[int(prev)] == search:
        return prev

    return -1;


arr = [1,2,4,5,7,8,12,15,16,18,22,35]
search = 18

result = jump_search(arr, search)

if result == -1:
    print("Element not found in array")
else:
    print("element found at index", result)