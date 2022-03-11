# 23. Merge k Sorted Lists


def mergeKLists(lists):
	'''
	1.
	time comp O(N * M) [N --> len of lists and M --> len of Linked list] space comp --> O(N + M)
	
	Make a temporary array to store all the elements
	sort the array
	make a new Linked List
	append all the array elements to it and return it.

	2.
	time comp --> O(N log(M)) space comp --> O(K)
	'''


	# Time comp --> O(N * lng(k))
	def merge(l1, l2):
        dummy = ListNode()
        tail  = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        while l1:
            tail.next = l1
            l1 = l1.next
            tail = tail.next
        
        while l2:
            tail.next = l2
            l2 = l2.next
            tail = tail.next
        
        return dummy.next


    # This is the main content
    if not lists or len(lists) == 0: return None
    
    while len(lists) > 1:
        mergedList = []
        
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if (i+1) < len(lists) else None
            
            temp = self.merge(l1, l2)
            mergedList.append(temp)
        
        lists = mergedList
    
    return lists[0]

    




	# temp = []
        
 #    for LinkedList in lists:
 #        while LinkedList:
 #            temp.append(LinkedList.val)
 #            LinkedList = LinkedList.next
    
 #    temp.sort()
 #    dummy = ListNode()
 #    tail = dummy
    
 #    for item in temp:
 #        tail.next = ListNode(item)
 #        tail = tail.next
    
 #    return dummy.next



if __name__ == '__main__':
	lists = [[1,4,5],[1,3,4],[2,6]]
	res = mergeKLists(lists)
	print(res)