import sys

class Graph ():
    def __init__(self, size, edges):
        #Edges of form [(0,1,5), (0,2,10)...] where it is a list of tuples of v1, v2, weight
        self.adjMatrix = [[0 for i in range(size)] for j in range(size)]
        self.numVertices = size

        for edge in edges:
            self.adjMatrix[edge[0]][edge[1]] = edge[2]
            self.adjMatrix[edge[1]][edge[0]] = edge[2] 
    

    def printMST(self, parent): 
        print("Edge \tWeight")
        for i in range(1, self.numVertices): 
            print(parent[i], "-", i, "\t", self.adjMatrix[i][ parent[i] ]) 

    def primMinKey(self, keys, mstSet):
        min = sys.maxsize
        min_index = -1

        for v in range(self.numVertices):
            if keys[v] < min and mstSet[v] == False:
                min = keys[v]
                min_index = v

        return min_index

    def primMST(self):
        #Stores the keys used to pick the next node to add to the MST
        keys = [sys.maxsize] * self.numVertices
        #Stores the parent of each node that is added to the MST to keep track of the tree
        parent = [None] * self.numVertices
        #Starting at 0, but MST can be calculated from anywhere
        keys[0] = 0
        #Initially, no nodes are part of the MST
        mstSet = [False] * self.numVertices

        for _ in range(self.numVertices):
            #Find min of the keys that will be added to the set
            u = self.primMinKey(keys, mstSet)
            #Set that we are adding this to the set
            mstSet[u] = True

            #check each vertex to see if the minimum one we are on has a connection and if it does check if that connection
            #is less than what is already entered as the shortest path into the MST for the node in keys
            #only works if the node is not already in the mst as well
            for v in range(self.numVertices):
                if self.adjMatrix[u][v] > 0 and mstSet[v] == False and keys[v] > self.adjMatrix[u][v]:
                    #since keys started out with all max sizes, then each node will hit this at least once to have an edge
                    #put a value into key and set its parent as something (except for the first node which will have parent of 0)
                    keys[v] = self.adjMatrix[u][v]
                    parent[v] = u
        self.printMST(parent)

if __name__=='__main__':
    e = [
        (0,1,4),
        (0,7,8),
        (1,2,8),
        (1,7,11),
        (7,6,1),
        (7,8,7),
        (2,3,7),
        (2,8,2),
        (2,5,4),
        (8,6,6),
        (6,5,2),
        (3,4,9),
        (3,5,14),
        (5,4,10)
    ]
    size = 9
    g = Graph(size, e)
    g.primMST()