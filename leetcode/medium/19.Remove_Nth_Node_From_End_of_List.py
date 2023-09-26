#https://leetcode.com/problems/remove-nth-node-from-end-of-list/

'''Given the head of a linked list,
remove the nth node from the end of the list
and return its head.'''

from typing import Optional

class ListNode:
    def __init__(self,val=0,next=None) -> None:
        self.val = val
        self.next = next
    def printValue(self):
        temp = self
        res = []
        while temp:
            res.append(temp.val)
            temp = temp.next
        print(res)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        l = dummy 
        r = head
        while r and n > 0:
            r = r.next 
            n -= 1
        while r:
            r = r.next
            l = l.next

        l.next = l.next.next
        return dummy.next 
        




if __name__ == "__main__":
    test1 = Solution()
    testNode = ListNode(val = 1,next = ListNode(val=2,next=ListNode(val=5,next=ListNode(val = 9))))
    testNode.printValue()
    test1.removeNthFromEnd(testNode,2).printValue()
