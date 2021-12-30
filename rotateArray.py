def reverseArray(arr, l, r):
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    
def rotateArray(arr, n, k):
    reverseArray(arr, 0, n-1)
    reverseArray(arr, 0, k-1)
    reverseArray(arr, k, n-1)

if __name__ == "__main__":
    k = 3
    arr = [1,2,3,4,5,6,7,8]
    n = len(arr)
    rotateArray(arr, n, k)

    print(arr)