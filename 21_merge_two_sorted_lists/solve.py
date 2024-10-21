from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # while both lists are not empty,
        # iterate through both lists simultaneously, append smaller val to newList
        # O(n + m)
        # if one list becomes empty, rest of other list is appended all at once
        
        # Assign newListHead
        newListHead = None
        if list2 is None:
            if list1 is None:
                return None
            else:
                return list1
        else:
            if list1 is None:
                return list2
            else:
                if list1.val > list2.val:
                    newListHead = list2
                    list2 = list2.next
                else:
                    newListHead = list1
                    list1 = list1.next

        # Body
        newListCurr = newListHead
        while list1 is not None and list2 is not None:
            if list1.val > list2.val:
                newListCurr.next = list2
                list2 = list2.next
            else:
                newListCurr.next = list1
                list1 = list1.next

            newListCurr = newListCurr.next

        # Append remaining
        if list1 is None:
            newListCurr.next = list2
        else:
            newListCurr.next = list1
        
        return newListHead

def main():
    x = Solution()

    y = ListNode(1)
    y.next = ListNode(2)
    y.next.next = ListNode(4)
    
    z = ListNode(1)
    z.next = ListNode(3)
    z.next.next = ListNode(4)
    z.next.next.next = ListNode(5)
    z.next.next.next.next = ListNode(6)
    z.next.next.next.next.next = ListNode(7)
    z.next.next.next.next.next.next = ListNode(8)
    z.next.next.next.next.next.next.next = ListNode(9)
    
    result = x.mergeTwoLists(y, z)
    while result is not None:
        print(result.val)
        result = result.next


if __name__ == "__main__":
    main()