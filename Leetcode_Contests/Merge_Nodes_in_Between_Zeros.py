# 2181. Merge Nodes in Between Zeros

# time comp --> O(N) space comp --> O(1)
def mergeNodes(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    tail  = dummy
    
    curNode = head
    while curNode:
        if curNode.val == 0:
            temp = curNode.val
            
            while curNode.next != None and curNode.next.val != 0:
                curNode = curNode.next
                print(temp)
                temp += curNode.val
            if temp:
                tail.next = ListNode(temp)
                tail = tail.next
            
        curNode = curNode.next
    
    return dummy.next

if __name__ == '__main__':
	head = [0,3,1,0,4,5,2,0]
	res = mergeNodes(head)
	print(res)