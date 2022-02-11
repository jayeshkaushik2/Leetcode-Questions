# import math
# n = -1

'''
when dealing with the -ve number to get the remainder and quotient -->:
Use the in-build function(libraries like math)

To get the remainder of the -ve number we can do --> math.fmod(number, denominator)
To ge the quotient of the -ve number we can do --> int(n / 10)
'''

# print(int(math.fmod(n, 10)), n % 10)

# print(int(n / 10), n // 10)

# print(2**31-1, -2**31)


def place(res, c):
	flag = False
	res = list(res)
	
	for i in range(len(res)):
		if ord(res[i]) > ord(c)+1:
			print(res[i], c)
			res.insert(i, c)
			flag = True
			break

	if flag:
		return "".join(res)
	else:
		res = "".join(res)
		res += c
		return res


def find(n, k):
	if (k == 1 and n > 1) or (n < k):
		return -1

	temp = []
	for i in range(k):
		temp.append(chr(i + ord('a')))

	while len(temp) < n:
		temp = temp + temp
	print(temp)

	res = ''
	j = 0
	for i in range(n):
		res = place(res, temp[j])
		j += 1

	return res


if __name__=='__main__':
	T = int(input())
	for i in range(T):
		arr = list(map(int, input().split()))
		n = arr[0]
		k = arr[1]
		res = find(n , k)
		print(res)


# def find(n):
# 	for i in range(1, n//2):
# 		n1 = i
# 		bc = n - n1

# 		for j in range(1, bc//2+1):
# 			n2 = j
# 			n3 = bc-j
# 			if n1^n2^n3 == 0:
# 				return str(i)+' '+str(n2)+' '+str(n3)


# 		# bc = n - i
# 		# if i^bc != 0:
# 		# 	for j in range(1, bc//2):
# 		# 		n2 = j
# 		# 		if bc-n2 <= 0:
# 		# 			break
# 		# 		n3 = bc-j
# 		# 		if i^n2^n3 == 0:
# 		# 			return str(i)+' '+str(n2)+' '+str(n3)

# 	return -1

# T = int(input())

# for i in range(T):
# 	n = int(input())
# 	res = find(n)
# 	print(res)


a, b, c = map(int, input().split())
