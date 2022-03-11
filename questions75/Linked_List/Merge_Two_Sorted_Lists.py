# 21. Merge Two Sorted Lists

# time comp --> O(N+M) space comp --> O(1)
def mergeTwoLists(list1, list2):
	dummy = ListNode()
	tail = dummy

	while list1 and list2:
		if list1.val < list2.val:
			tail.next = ListNode(list1.val)
			tail = tail.next
			list1 = list1.next
		else:
			tail.next = ListNode(list2.val)
			tail = tail.next
			list2 = list2.next

	while list1:
		tail.next = ListNode(list1.val)
		tail = tail.next
		list1 = list1.next

	while list2:
		tail.next = ListNode(list2.val)
		tail = tail.next
		list2 = list2.next

	return dummy.next


if __name__ == '__main__':
	list1 = [1,2,4]
	list2 = [1,3,4]
	res = mergeTwoLists(list1, list2)
	print(res)