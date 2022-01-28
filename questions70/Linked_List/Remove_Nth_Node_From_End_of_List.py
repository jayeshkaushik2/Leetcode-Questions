# 19. Remove Nth Node From End of List


def removeNthFromEnd(head, n):
	# optimized solution 
	# time comp --> O(N) space comp --> O(1)
	dummy = ListNode(0, head)
	left = dummy
	right = head

	while n > 0 and right:
		right = right.next
		n -= 1

	while right:
		left = left.next
		right = right.next

	left.next = left.next.next

	return dummy.next

	# Brute force solution
	# time comp --> O(N) space comp --> O(N)
    # size = 0
    # curNode = head
    # temp = []
    
    # while curNode:
    #     size += 1
    #     temp.append(curNode.val)
    #     curNode = curNode.next
    
    # dummy = ListNode()
    # tail  = dummy
    
    # for i in range(size):
    #     if size-i == n:
    #         continue
    #     else:
    #         tail.next = ListNode(temp[i])
    #         tail = tail.next
    
    # return dummy.next

if __name__ == '__main__':
	head = [1,2,3,4,5]
	n = 2
	res = removeNthFromEnd(head, n)
	print(res)