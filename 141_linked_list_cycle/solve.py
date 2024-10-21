from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # visited array // Not constant memory
        # slow and fast pointer
        slow = head
        fast = head
        i = 1
        while slow is not None and fast is not None:
            if i % 2 == 0:
                slow = slow.next
                i -= 1
            else:
                i += 1

            fast = fast.next

            if slow == fast:
                return True
        
        return False

def main():
    x = Solution()
    print(x.hasCycle(None))

if __name__ == "__main__":
    main()