from typing import List
class Node():
    def __init__(self, val = 0, neighbours = None):
        self.val = val
        self.neighbours = neighbours if neighbours is not None else []

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodes = []
        for i in range(numCourses):
            nodes.append(None)
        print(nodes)
        
        for pr in prerequisites:
            course = pr[0]
            p = pr[1]
            if nodes[course] is None:
                courseNode = Node(course)
                nodes[course] = courseNode
            else:
                courseNode = nodes[course]
            if nodes[p] is None:
                pNode = Node(p)
                nodes[p] = pNode
            else:
                pNode = nodes[p]
            
            pNode.neighbours.append(courseNode)
        
        return self.findCycle(nodes)
    
    def findCycle(nodes: List['Node']) -> bool:
        

def main():
    x = Solution()
    print(x.canFinish(2, [[1,0]]))
    print(x.canFinish(2, []))
    print(x.canFinish(2, [[1,0],[0,1]]))
    print(x.canFinish(3, [[1,0],[0,1]]))
    print(x.canFinish(3, [[1,0],[2,0],[2,1]]))
    print(x.canFinish(3, [[0,1],[1,2],[2,0]]))


if __name__ == "__main__":
    main()