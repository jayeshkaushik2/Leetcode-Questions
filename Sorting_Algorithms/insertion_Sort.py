# Remember it by card problem
'''
sorting algorithm time comp --> O() space comp --> O()
best case
'''
def insertion_Sort(arr, n) -> None:
    # we are not swaping the elements, we are swifting the elements
    if arr == []: return None

    '''
    using while loop
    while loop is much better in insertion sorting
    '''
    # i = 1
    # while i < n:
    #     temp = arr[i]
    #     j = i - 1
    #     while j >= 0:
    #         if arr[j] > temp:
    #             arr[j+1] = arr[j]
    #             j -= 1
    #         else:
    #             break
        
    #     arr[j+1] = temp
    #     i += 1

    '''
    using for loop
    '''
    for i in range(1, n):
        temp = arr[i]
        j = i-1
        for j in range(j, -2, -1):
            if temp < arr[j]:
                arr[j+1] = arr[j]
            else:
                print(j)
                break
        arr[j+1] = temp
        


if __name__ == "__main__":
    arr = [9,8,7,6,5,4,3,2,1,0]
    n   = len(arr)
    print(arr)
    insertion_Sort(arr, n)
    print(arr)