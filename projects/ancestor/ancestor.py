# from projects.graph.graph import Graph
from util import Stack

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id in self.vertices:
            print("vertex already exists")
        else:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """

        if v1 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def find_ancestors(self, starting_vertex):
        s = Stack()
        result = set()
        s.push(starting_vertex)
        visited = set()
        while s.size() > 0:
            current_node = s.pop()
            if current_node not in visited:
                visited.add(current_node)
                neighbors = self.get_neighbors(current_node)
                if len(neighbors) == 0 and current_node != starting_vertex:
                    result.add(current_node)

                for neighbor in neighbors:
                    s.push(neighbor)
        return result

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        visited = set()
        path = [starting_vertex]
        s.push(path)
        while s.size() > 0:
            current_path = s.pop()
            current_node = current_path[-1]
            if current_node == destination_vertex:
                return current_path
            if current_node not in visited:
                visited.add(current_node)
                neighbors = self.get_neighbors(current_node)
                for neighbor in neighbors:
                    neighbor_path = current_path.copy()
                    neighbor_path.append(neighbor)
                    s.push(neighbor_path)


def earliest_ancestor(ancestors, starting_node):
    # Break out ancestors, reverse orders, populate vertex and edges.
    aGraph = Graph()

    # create vertex set
    vertex = set()
    res_path = []
    result = -1
    for ancestor in ancestors:
        for v in ancestor:
            vertex.add(v)
    # add vertex to graph
    for v in vertex:
        aGraph.add_vertex(v)

    # reverse order of edges, child leads to parent

    for ancestor in ancestors:
        aGraph.add_edge(ancestor[1], ancestor[0])
    # find eldest ancestors

    elders = aGraph.find_ancestors(starting_node)
    # print("elders ", elders)

    for elder in elders:
        new_path = aGraph.dfs(starting_node, elder)
        # print(elder, len(res_path))
        if len(new_path) > len(res_path):
            res_path = new_path
            result = new_path[-1]

        if len(new_path) == len(res_path) and new_path[-1] < res_path[-1]:
            res_path = new_path
            result = new_path[-1]

    # print(aGraph.dfs(starting_node, elder))
    return result

    # compare paths
    # return proper response
# print(earliest_ancestor(test_ancestors, 11))
