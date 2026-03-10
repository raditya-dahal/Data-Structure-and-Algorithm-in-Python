"""
Implement a BFS traversal function for a graph
With the information you have received from the course, implement a Breadth-First traversal iterative function for a graph.
 The function accepts as parameters the graph object and the vertex from where to start .

The function should return a dictionary with the vertices as the keys and the vertices from where those keys where visited 
as the values.
For example:

Test	Result
A = Vertex('A')
B = Vertex('B')
C = Vertex('C')
D = Vertex('D')
E = Vertex('E')
F = Vertex('F')

AB = Edge(A, B, 2)
AC = Edge(A, C, 4)
BD = Edge(B, D, 5)
CD = Edge(C, D, 9)
CE = Edge(C, E, 3)
DF = Edge(D, F, 2)
EF = Edge(E, F, 2)

adj_map = {
    A: { B: AB, C: AC },
    B: { A: AB, D: BD }, 
    C: { A: AC, D: CD, E: CE },
    D: {B: BD, C: CD, F: DF},
    E: {C: CE, F: EF},
    F: {D: DF, E: EF}
}

g = Graph(adj_map)
print(BFS(g, A))
{<Vertex: A>: None, <Vertex: B>: <Vertex: A>, <Vertex: C>: <Vertex: A>, <Vertex: D>: <Vertex: B>, <Vertex: E>: 
<Vertex: C>, <Vertex: F>: <Vertex: D>}"""

from collections import deque

def BFS(graph, start):
    # Initialize visited dictionary with start node
    visited = {start: None}
    
    # Use a queue for BFS
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        
        # Explore neighbors
        for neighbor in graph._adj_map[current]:
            if neighbor not in visited:
                visited[neighbor] = current  # Set parent
                queue.append(neighbor)
    
    return visited