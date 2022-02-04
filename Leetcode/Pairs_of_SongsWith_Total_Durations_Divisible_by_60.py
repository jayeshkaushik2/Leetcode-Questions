# 1010. Pairs of Songs With Total Durations Divisible by 60



# time comp --> O(N^2) space comp --> O(1)
def numPairsDivisibleBy60(time):
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