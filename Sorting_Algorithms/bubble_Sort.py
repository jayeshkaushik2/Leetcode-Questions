#  sorting algorithm time comp --> O(n^2) space comp --> O(1)

def bubble_Sort(arr, n) -> None:
    # this solution is not optimized
    # for i in range(n):
    #     for j in range(1, n):
    #         if arr[j] < arr[j-1]:
    #             arr[j], arr[j-1] = arr[j-1], arr[j]

    '''
    optimized slution is 
    ist way i --> [1 to n) and j --> [0 to n-i)
    2nd way i --> [0 to n-1) and j --> [0 to n-i-1) ---OR--- i --> [0 to n) and j --> [1 to n-1)
    we can check if there is any swaps are not it no swaps are done than array is already sorted
    best case --> O(n)
    worst case --> O(n^2)
    '''
    for i in range(1, n):
        swap = False
        for j in range(0, n-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if swap == False:
            break

if __name__ == "__main__":
    arr = [9,8,7,6,5,4,3,2,1,0]
    n = len(arr)
    print(arr)
    bubble_Sort(arr, n)
    print(arr)