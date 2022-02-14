# 2169. Count Operations to Obtain Zero

# time comp --> O(N) space comp --> O(1)
def countOperations(num1: int, num2: int) -> int:
        cnt = 0
        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            cnt += 1
        
        return cnt

if __name__=='__main__':
	num1 = 2
	num2 = 3
	res = countOperations(num1, num2)
	print(res)