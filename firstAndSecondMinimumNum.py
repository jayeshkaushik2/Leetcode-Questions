def FirstTowMinimumNumber(arr, n):
    min1 = arr[0]
    min2 = 1000000

    for i in range(1, n):
        if arr[i] < min1:
            min2 = min1
            min1 = arr[i]
        elif arr[i] < min2 and arr[i] != min1:
            min2 = arr[i]
    
    return [min1, min2]

if __name__ == '__main__':
    arr = [2,1,3,4,5,6,0]
    n = len(arr)
    ans = FirstTowMinimumNumber(arr, n)
    print(ans)