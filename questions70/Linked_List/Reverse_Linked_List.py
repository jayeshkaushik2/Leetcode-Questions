# 206. Reverse Linked List

def reverseList(head):
	'''
	There are two solutions
	1) time comp --> O(N) space comp --> O(1)
	2) time comp --> O(N) space comp --> O(N)
	'''
	prevNode = None
	currNode = head
	nextNode = None

	while curNode:
		nextNode = currNode.next
		currNode.next = prevNode

		prevNode = currNode
		currNode = nextNode

	return pervNode



	# temp = []
	# while head:
	# 	temp.append(head.val)
	# 	head = head.next

	# temp = temp[::-1]
	# dummy = ListNode()
	# tail = dummy

	# for item in temp:
	# 	tail.next = ListNode(item)
	# 	tail = tail.next
	# return dummy.next


if __name__ == '__main__':
	head = [1,2,3,4,5]
	res = reverseList(head)
	print(res)