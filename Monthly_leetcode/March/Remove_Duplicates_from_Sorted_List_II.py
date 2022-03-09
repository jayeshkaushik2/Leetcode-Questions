# 82. Remove Duplicates from Sorted List II

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
	# time comp --> O(N) space comp --> O(1)
	dummy = ListNode(0, head)
	prev = 	dummy
	while head:
	    if head.next != None and head.val == head.next.val:
	        while head.next and head.val == head.next.val:
	            head = head.next
	        prev.next = head.next
	    else:
	        prev = prev.next
	    head = head.next
	    
	return dummy.next




	# time comp --> O(N) space comp --> O(N)
	curNode = head
	dummy = ListNode()
	tail = dummy
	temp = []

	while curNode:
	    if curNode.next and curNode.val == curNode.next.val:
	        temp.append(curNode.val)
	    if curNode.val not in temp:
	        tail.next = ListNode(curNode.val)
	        tail = tail.next
	    
	    curNode = curNode.next
	    
	return dummy.next




	# time comp --> O(N) space comp --> O(2N)
	curNode = head
	hm = {}

	while curNode:
	    if curNode.val in hm:
	        hm[curNode.val] += 1
	    else:
	        hm[curNode.val] = 1
	    curNode = curNode.next
	
	temp = []
	for item in hm:
	    if hm[item] == 1:
	        temp.append(item)
	temp.sort()
	
	dummy = ListNode()
	tail = dummy
	for item in temp:
	    tail.next = ListNode(item)
	    tail = tail.next
	
	return dummy.next


if __name__ == '__main__':
	head = [1,2,3,3,4,4,5]
	res = deleteDuplicates(head)
	print(res)