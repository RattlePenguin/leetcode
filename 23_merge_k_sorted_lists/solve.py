from typing import Optional, List
import heapq # min heap
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for list in lists:
            while list is not None:
                elem = list.val
                heapq.heappush(heap, elem)
                list = list.next
        
        result = None
        while len(heap) > 0:
            elem = heapq.heappop(heap)
            new = ListNode(elem)
            if result is None:
                result = new
                curr = result
                continue
            curr.next = new
            curr = curr.next

        return result

def main():
    x = Solution()
    new1 = ListNode(1)
    param1 = [new1]
    print(x.mergeKLists(param1))
    print(x.mergeKLists([]))


if __name__ == "__main__":
    main()