from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        l3 = ListNode(0)
        l3curr = l3
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
            if l2:
                sum += l2.val

            sum += carry
            new = ListNode(sum % 10)
            carry = sum // 10
            l3curr.next = new
            l3curr = l3curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        return l3.next

def main():

if __name__ == "__main__":
    main()
