#https://leetcode.com/problems/middle-of-the-linked-list/

'''Given the head of a singly linked list,
return the middle node of the linked list.

If there are two middle nodes,
return the second middle node'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def printValue(self):
        res = [] 
        temp = self
        while temp:
            res.append(temp.val)
            temp = temp.next
        print(res)
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dictNode = []
        temp = head
        while temp:
            dictNode.append(temp)
            temp = temp.next
        return dictNode[len(dictNode) // 2]

        
if __name__ == "__main__":
    test1 = Solution()
    testNode = ListNode(val = 1,next = ListNode(val=2,next=ListNode(val=5,next=ListNode(val = 9))))
    testNode.printValue()
    test1.middleNode(testNode).printValue()
