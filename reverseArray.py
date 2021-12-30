def reverseArray(arr, n):
    s = 0
    e = n-1
    while s < e:
        arr[s], arr[e] = arr[e], arr[s]
        s += 1
        e -= 1

arr = [1,2,3,4,5,6,7,8,9]
reverseArray(arr, 9)
print(arr)