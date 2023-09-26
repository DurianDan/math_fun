# https://leetcode.com/problems/merge-two-sorted-lists/discuss/9754/my-easy-python-solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def print_list(self):
        linked_list = []
        test = self 
        while True:
            linked_list.append(test.val)
            if not test.next: break 
            test = test.next
        print(linked_list)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merge_list = ListNode()
        cur = merge_list
        
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next 
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2
        return cur

if __name__ == "__main__":
    node1 = ListNode(val = 1,next= ListNode(val = 1,next = ListNode(val = 4)))    
    node2 = ListNode(val = 2,next= ListNode(val = 3,next = ListNode(val = 5)))    
    test1 = Solution()
    test1.mergeTwoLists(node1,node2).print_list()
