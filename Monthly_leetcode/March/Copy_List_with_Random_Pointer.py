# 138. Copy List with Random Pointer

def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
	# time comp --> O(N) space comp --> O(N)
	hm = { None:None }
	curNode = head
	while curNode:
	    copy = Node(curNode.val)
	    hm[curNode] = copy
	    curNode = curNode.next
	
	curNode = head
	while curNode:
	    copy = hm[curNode]
	    copy.next = hm[curNode.next]
	    copy.random = hm[curNode.random]
	    curNode = curNode.next
	
	return hm[head]






	# time comp --> O(N) space comp --> O(N)
	# first make a clone linkedlist
	curNode = head
	cloneList = ListNode()
	tail = cloneList
	while curNode:
	    tail.next = Node(curNode.val)
	    tail = tail.next
	    curNode = curNode.next
	
	# create a hashmap for the random pointer
	oldToNew = {}
	curNode = head
	cloneCurNode = cloneList.next
	while curNode:
	    oldToNew[curNode] = cloneCurNode
	    curNode = curNode.next
	    cloneCurNode = cloneCurNode.next
	
	# Now assign the random pointer
	curNode = head
	cloneCurNode = cloneList.next
	while curNode:
	    cloneCurNode.random = oldToNew[curNode.random] if curNode.random else None
	    curNode = curNode.next
	    cloneCurNode = cloneCurNode.next
	
	return cloneList.next

if __name__ == '__main__':
	head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
	res = copyRandomList(head)
	print(res)