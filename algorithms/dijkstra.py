import sys

class Graph ():
    def __init__(self, size, edges):
        #Edges of form [(0,1,5), (0,2,10)...] where it is a list of tuples of v1, v2, weight
        self.adjMatrix = [[0 for i in range(size)] for j in range(size)]
        self.numVertices = size

        for edge in edges:
            self.adjMatrix[edge[0]][edge[1]] = edge[2]
            self.adjMatrix[edge[1]][edge[0]] = edge[2] 

    def printSolution(self, dist): 
        print("Vertex \tDistance from Source")
        for node in range(self.numVertices): 
            print(node, "\t", dist[node]) 

    def findLeastDistance(self, dist, sps):
        minDistIndex = 0
        minDist = sys.maxsize
        for i in range(len(dist)):
            if dist[i] < minDist and i not in sps:
                minDistIndex = i
                minDist = dist[i]
        return minDistIndex
        
    def dijkstra(self, startNode=0):
        #init dist array and shortest path set 
        dist = [sys.maxsize] * self.numVertices
        dist[startNode] = 0
        shortestPathSet = set()

        #iterate a number of times based on num vertices to make sure we check them all
        for _ in range(self.numVertices):
            #Find the minimum distance in the dist set to check next to see if it has a shorter path to adjacent nodes than they currently have
            u = self.findLeastDistance(dist, shortestPathSet)

            #mark the node we are anchoring on as in the shortest path set
            shortestPathSet.add(u)

            #for the num of vertices we are going to check the row associated with the anchored vertex we are checking to see if it has edges to other vertices to check for shorter path
            for v in range(self.numVertices):
                if self.adjMatrix[u][v] > 0 and v not in shortestPathSet:
                    if self.adjMatrix[u][v] + dist[u] < dist[v]:
                        #if the distance from the edge of anchored noe to source plus the edge is less than the current shortest path to another node that has not had shortest path found
                        #then set the new distance to the dist array
                        dist[v] = self.adjMatrix[u][v] + dist[u]
        self.printSolution(dist)

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
    g.dijkstra(0)
