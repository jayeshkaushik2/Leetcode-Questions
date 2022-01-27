# 141. Linked List Cycle


# time comp --> O(N) space comp --> O(1)
def hasCycle(head):
	if head is None: return False

	fast = head
	slow = head.next

	while fast != slow:
		if fast is None or fast.next is None: return False

		fast = fast.next.next
		slow = slow.next

	return True


if __name__ == '__main__':
	head = [3,2,0,-4]
	res = hasCycle(head)
	print(res)