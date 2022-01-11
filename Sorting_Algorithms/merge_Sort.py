arr = [2,5,3,4,1,9,6]
n = len(arr)

def merge(arr, l ,m, r):
    n1 = m-l+1
    n2 = r-m
    l1 = [0]*n1
    r1 = [0]*n2
    for i in range(n1):
        l1[i] = arr[i+l]
    for j in range(n2):
        r1[j] = arr[m+j+1]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if l1[i] < r1[j]:
            arr[k] = l1[i]
            i += 1
        else:
            arr[k] = r1[j]
            j += 1
        k += 1
    
    if i >= n1:
        while j < n2:
            arr[k] = r1[j]
            j += 1
            k += 1
    else:
        while i < n1:
            arr[k] = l1[i]
            i += 1
            k += 1


def mergesort(arr, l, r):
    if l < r:
        mid = int((l+r)/2)
        mergesort(arr, l, mid)
        mergesort(arr, mid+1, r)
        merge(arr, l, mid, r)

mergesort(arr, 0, n-1)
print(arr)