# 206. Reverse Linked List

def reverseList(head):
	'''
	there are two approaches
	1. Itrative time comp --> O(N) space comp --> O(1)
	2. Recursive time comp --> O(N) space comp --> O(N) 
	'''

	# Recursive
	# base case
	if head is None or head.next is None:
		return head

	newHead = reverseList(head.next)
	headNext = head.next
	headNext.next = head
	head.next = next

	return newHead



	# Itrative
	prevNode = None
	currNode = head

	while currNode:
		nextNode = curNode.next

		currNode.next = prevNode
		preNode = currNode
		currNode = nextNode

	return prevNode



if __name__ == '__main__':
	head = [1,2,3,4,5,6]
	res = reverseList(head)
	print(head)