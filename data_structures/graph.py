from collections import deque

class Graph():
    def __init__(self, size):
        self.graph = [[0 for i in range(size)] for j in range(size)]
        self.size = size
    
    def __str__(self):
        ret = ""
        for i in range(self.size):
            ret += (str(self.graph[i]) + "\n")
        return(ret)

    def addEdge(self, n1, n2, w=1):
        try:
            self.graph[n1][n2] = w
            self.graph[n2][n1] = w
            return True
        except IndexError:
            return False

    def interactiveEdgeAdding(self):
        print(f"The current graph of size {self.size} is: ")
        print(self)
        exit = False
        while not exit:
            n1 = int(input("Enter first node of edge: "))
            n2 = int(input("Enter second node of edge: "))
            w = int(input("Enter the weight of edge: "))
            succ = self.addEdge(n1, n2, w)
            if succ:
                print("Node added successfully")
            else:
                print("Index of nodes out of bounds for size of graph")
            cont = input("Enter yes/no to create another or quit: ").lower()
            while cont not in ["yes", "no"]:
                cont = input("Enter yes/no to create another or quit: ").lower()
            exit = False if cont == "yes" else True 

    def dfs(self, startNode):
        retList = []
        visited = set()
        def dfs_util(node):
            if node not in visited:
                visited.add(node)
                retList.append(node)
                for i in range(self.size):
                    if self.graph[node][i] > 0:
                        dfs_util(i)
        dfs_util(startNode)
        return retList
    
    def bfs(self, startNode):
        q = deque()
        q.append(startNode)
        retList = []
        visited = set()
        while len(q) > 0:
            node = q.popleft()
            retList.append(node)
            for i in range(self.size):
                if self.graph[node][i] > 0 and i not in visited:
                    q.append(i)
                    visited.add(i)
        return retList
        
if __name__=='__main__':
    g = Graph(10)
    g.interactiveEdgeAdding()
    print(g)
    print(g.dfs(0))
    print(g.bfs(0))