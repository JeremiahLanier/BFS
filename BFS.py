from collections import defaultdict

class Graph:

    def __init__(self):

        self.graph = defaultdict(list)

    def addEdges(self,j,l):
        self.graph[j].append(l)

    def BFS(self, r):

        visited = [False] * (len(self.graph))

        queue = []

        queue.append(r)
        visited[r] = True

        while queue:
            r =  queue.pop(0)
            print(r, end = "")


            for i in self.graph[r]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True



g = Graph()
g.addEdges(0,1)
g.addEdges(0,2)
g.addEdges(1,2)
g.addEdges(2,0)
g.addEdges(2,3)
g.addEdges(3,3)


print ("Breadth First Traversal")

g.BFS(2)