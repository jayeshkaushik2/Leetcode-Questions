# Merge_Two_Sorted_LinkedLists

# time comp --> O(N + M) space comp --> O(1)
def mergeTwoLists(list1, list2):
	dummy = ListNode()
	tail = dummy
	
	while list1 and list2:
	    if list1.val < list2.val:
	        tail.next = list1
	        list1 = list1.next
	    else:
	        tail.next = list2
	        list2 = list2.next
	    tail = tail.next
	
	if list1 is not None:
	    tail.next = list1
	    tail = tail.next
	
	if list2 is not None:
	    tail.next = list2
	    tail = tail.next
	
	return dummy.next

if __name__ == '__main__':
	list1 = [1,4,5]
	list2 = [2,3,6]
	res = mergeTwoLists(list1, list2)
	print(res)