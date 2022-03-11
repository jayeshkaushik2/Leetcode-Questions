# 61. Rotate List

def rotateRight(head, k):
	# time comp --> O(N) space comp --> O(1)
	if head is None: return head
	
	n = 1
	tail = head
	while tail.next:
	    n += 1
	    tail = tail.next
	
	k = k % n
	if k == 0:
	    return head
	
	curNode = head
	for i in range(n-k-1):
	    curNode = curNode.next
	
	temp = curNode.next
	curNode.next = None
	tail.next = head
	
	return temp




	# time comp --> O(N + K) space comp --> O(N)
	if k == 0 or head is None:
	    return head
	
	n = 0
	curNode = head
	temp = []
	while curNode:
	    n += 1
	    temp.append(curNode.val)
	    curNode = curNode.next
	
	k = k % n
	for i in range(k):
	    ele = temp.pop()
	    temp.insert(0, ele)
	    
	dummy = ListNode()
	tail = dummy
	for ele in temp:
	    tail.next = ListNode(ele)
	    tail = tail.next
	
	return dummy.next
if __name__ == '__main__':
	head = [1,2,3,4,5]
	k = 2
	res = rotateRight(head, k)
	print(head)