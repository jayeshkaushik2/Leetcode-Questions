'''
assert is used to check the condition is true or not
true --> run the next line
false --> throws the assertionError: the msg we write in the assert line
'''

def fact(n):
	assert n >= 0 and int(n) == n, "this is not a valid input!"
    if n in [0,1]:
        return 1
    else:
        return n*fact(n-1)

print(fact(-5))