# 141. Linked List Cycle

# time comp --> O(N) space comp --> O(1)
def hasCycle(head: ListNode) -> bool:
	slow, fast = head, head
	
	while fast and fast.next:
	    slow = slow.next
	    fast = fast.next.next
	    if slow == fast:
	        return 1
	
	return 0


if __name__ == '__main__':
	head = [1,2,3,4,2]
	res = hasCycle(head)
	print(res)