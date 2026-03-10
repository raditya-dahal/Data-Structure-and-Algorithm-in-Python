"""
Implement a DFS traversal function for a graph
With the information you have received from the course, implement a Depth-First traversal recursive function for a graph. 
The function accepts as parameters the graph object, the vertex from where to start and a visited dictionary 
(that defaults to None, so the final user don't need to provide it)

The function should return a dictionary with the vertices as the keys and the vertices from where those keys where 
visited as the values.

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
print(DFS(g, A))
{<Vertex: A>: None, <Vertex: B>: <Vertex: A>, <Vertex: D>: <Vertex: B>, <Vertex: C>: <Vertex: D>, <Vertex: E>: <Vertex: 
C>, <Vertex: F>: <Vertex: E>}
"""

def DFS(graph, start, visited=None):
    # Initialize visited dictionary on first call
    if visited is None:
        visited = {start: None}

    # Explore neighbors
    for neighbor in graph._adj_map[start]:
        if neighbor not in visited:
            visited[neighbor] = start
            DFS(graph, neighbor, visited)

    return visited