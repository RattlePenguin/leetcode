# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional, List
class Solution:
    def dfs(self, node: Optional['Node'], curr: Optional['Node'], visited: List[int], nodes: List['Node']) -> Optional['Node']:
        visited[curr.val] = True
        for nb in node.neighbors:
            if visited[nb.val] is True:
                if nodes[nb.val] not in curr.neighbors:
                    curr.neighbors.append(nodes[nb.val])
                    nodes[nb.val].neighbors.append(curr)        
                continue
            newNb = Node(nb.val)
            curr.neighbors.append(newNb)
            newNb.neighbors.append(curr)
            nodes[newNb.val] = newNb
            
            self.dfs(nb, newNb, visited, nodes)
        return curr

        
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        new = Node(node.val)
        visited = []
        nodes = []
        for i in range(101):
            visited.append(False)
            nodes.append(None)

        nodes[new.val] = new
        return self.dfs(node, new, visited, nodes)


def main():
    x = Solution()

    

if __name__ == "__main__":
    main()