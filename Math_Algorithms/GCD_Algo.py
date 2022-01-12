'''
two ways recursive and itrative
'''
# itrative algo
def gcd(a, b) -> int:
    if a == 0:
        return b
    
    if b == 0:
        return a

    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a
    
    return a

if __name__ == '__main__':
    a = 72
    b = 24
    res = gcd(a, b)
    print(res)