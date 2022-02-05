# 1010. Pairs of Songs With Total Durations Divisible by 60

# Best solution is the second bcz --> time comp --> O(N) space comp --> O(1)
def numPairsDivisibleBy60(time):
    # This solution uses dictonary time comp --> O(N) space comp --> O(N)
    hm = {}
    count = 0

    for ele in time:
        # calculate the remainder of element
        rem = ele % 60

        if rem in hm:
            count += hm[rem]

        # calculate the mirror of the element --> 60 - rem
        temp = (60 - rem) % 60
        if temp in hm:
            hm[temp] += 1
        else:
            hm[temp] = 1

    return count




    # This solution uses array time comp --> O(N) space comp --> O(1) bcz[60]
    # calculate the remainders count from the time and store them in the array
    arr = [0]*60
    for temp in time:
        arr[temp%60] += 1

    count = 0
    # consider the edge cases like 0 and 30 for them count will be n(n-1)/2
    count += ((arr[0]-1) * arr[0])//2
    count += ((arr[30]-1) * arr[30])//2

    # now consider the other elements from 1 to 29 range
    for i in range(1, 30):
        # measure the product of element and its mirror
        product = arr[i] * arr[60-i]
        count += product

    return count




    # time comp --> O(N^2) space comp --> O(1)
    # this solution will through TLE
    pair = 0
    time.sort()
    n = len(time)
        
    for i in range(n):
        for j in range(i+1, n):
            if (time[i]+time[j])%60 == 0:
                pair += 1

    return pair


if __name__ == '__main__':
	time = [30,20,150,100,40]
	res = numPairsDivisibleBy60(time)
	print(res)