# 2. Add Two Numbers

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
	# time comp --> O(N+M) space comp --> O(1)
	dummy = ListNode()
	tail = dummy
	
	carry = 0
	while l1 or l2 or carry:
	    v1 = l1.val if l1 else 0
	    v2 = l2.val if l2 else 0
	    
	    sumis = v1 + v2 + carry
	    
	    carry = sumis // 10
	    sumis = sumis % 10
	    tail.next = ListNode(sumis)
	    
	    tail = tail.next
	    l1 = l1.next if l1 else None
	    l2 = l2.next if l2 else None
	
	return dummy.next
	
	
	# time comp --> O(N+M) space comp --> O(N+M)
	a1 = []
	a2 = []
	
	curNode = l1
	while curNode:
	    a1.append(curNode.val)
	    curNode = curNode.next
	
	curNode = l2
	while curNode:
	    a2.append(curNode.val)
	    curNode = curNode.next
	
	a1.reverse()
	a2.reverse()
	n1 = ""
	n2 = ""
	for n in a1:
	    n1 += str(n)
	n1 = int(n1)
	
	for n in a2:
	    n2 += str(n)
	n2 = int(n2)
	
	sumis = str(n1+n2)
	sumis = sumis[::-1]
	
	dummy = ListNode()
	tail = dummy
	
	for n in sumis:
	    tail.next = ListNode(n)
	    tail = tail.next
	
	return dummy.next


if __name__ == '__main__':
	l1 = [2,4,3]
	l2 = [5,6,4]
	res = addTwoNumbers(l1, l2)
	print(res)