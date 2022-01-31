# 143. Reorder List

# time comp --> O(N) space comp --> O(1)
def reorderList(head):
	'''
	first find the middle of the linked list and seprate them
	reverse the second linked list
	merge both linked lists together
	'''

	# find the middle of the linked list using slow and fast pointer
	slow, fast = head, head.next
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next

	second = slow.next
	# this is to make a partition
	slow.next = None
	# reverse the second linked list
	prevNode = None
	while second:
		nextNode = second.next

		second.next = prevNode
		prevNode = second
		second = nextNode

	# merging the two linked list in reorder
	first, second = head, prevNode
	# second will always be less then or equal to first
	while second:
		tmp1, tmp2 = first.next, second.next
		first.next = second
		second.next = tmp1
		first, second = tmp1, tmp2


if __name__ == '__main__':
	head = [1,2,3,4]
	# Output: [1,4,2,3]
	res = reorderList(head)
	print(res)