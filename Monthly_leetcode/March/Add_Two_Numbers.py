# 2. Add Two Numbers

def addTwoNumbers(l1, l2):
	# time comp --> O(N+M) space comp --> O(1)
	carry = 0
	dummy = ListNode()
	tail  = dummy
	while l1 or l2 or carry:
	    v1 = l1.val if l1 else 0
	    v2 = l2.val if l2 else 0
	    sumIs = v1 + v2 + carry
	    digit = sumIs % 10
	    carry = sumIs // 10
	    
	    tail.next = ListNode(digit)
	    tail = tail.next
	    
	    l1 = l1.next if l1 else None
	    l2 = l2.next if l2 else None
	    
	return dummy.next



	# time comp --> O(N+M) space comp --> O(1)
	dummy = ListNode()
	tail  = dummy
	carry = 0
	
	while l1 and l2:
	    sumIs = l1.val + l2.val + carry
	    digit = sumIs % 10
	    carry = sumIs // 10
	    tail.next = ListNode(digit)
	    tail = tail.next
	    l1 = l1.next
	    l2 = l2.next
	
	while l1:
	    sumIs = l1.val + carry
	    digit = sumIs % 10
	    carry = sumIs // 10
	    tail.next = ListNode(digit)
	    tail = tail.next
	    l1 = l1.next
	
	while l2:
	    sumIs = l2.val + carry
	    digit = sumIs % 10
	    carry = sumIs // 10
	    tail.next = ListNode(digit)
	    tail = tail.next
	    l2 = l2.next
	    
	if carry:
	    tail.next = ListNode(carry)
	    tail = tail.next
	
	return dummy.next

if __name__ == '__main__':
	l1 = [2,3,4]
	l2 = [1,2,3]
	res = addTwoNumbers(l1, l2)
	print(res)