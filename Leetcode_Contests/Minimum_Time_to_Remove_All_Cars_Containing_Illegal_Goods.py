# 6003. Minimum Time to Remove All Cars Containing Illegal Goods


def minimumTime(s: str) -> int:
	left_cost = [0]
	to_ret = 2*len(s)
	for i, t in enumerate(s) :
	    if t == '0' :
	        left_cost.append(left_cost[-1])
	    else :
	        left_cost.append(min(left_cost[-1]+2, i+1))
	    to_ret = min(to_ret, left_cost[-1]+(len(s)-i-1))
	
	# print(left_cost)
	return to_ret


if __name__ == '__main__':
	s = "1100101"
	res = minimumTime(s)
	print(res)