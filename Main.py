import math
n = -1

'''
when dealing with the -ve number to get the remainder and quotient -->:
Use the in-build function(libraries like math)

To get the remainder of the -ve number we can do --> math.fmod(number, denominator)
To ge the quotient of the -ve number we can do --> int(n / 10)
'''

print(int(math.fmod(n, 10)), n % 10)

print(int(n / 10), n // 10)

print(2**31-1, -2**31)