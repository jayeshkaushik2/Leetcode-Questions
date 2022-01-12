'''
sieve of eratosthenes : this algorithm is used to find prime numbers is a optimized way
time comp --> O(N x log(log(N))) space comp --> O(N)
'''

def Count_prime_numbers(n) -> int:
    cnt = 0
    primeNumbers = [True]*(n+1)
    primeNumbers[0] = False

    for i in range(2, n):
        if primeNumbers[i]:
            cnt += 1
        for j in range(i*2, n, i):
            primeNumbers[j] = False
    
    return cnt

if __name__ == '__main__':
    n = int(input())
    res = Count_prime_numbers(n)
    print(res)