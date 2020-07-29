# from projects.graph.graph import Graph
from graph import Graph

testing = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
           (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

aGraph = Graph()


def earliest_ancestor(ancestors, starting_node):
    # Break out ancestors, reverse orders, populate vertex and edges.

    # create vertex set
    vertex = set()
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
    aGraph.dft_recursive(starting_node)


    # depth first traversal
    # return longest path
    # compare paths
    # return proper response
earliest_ancestor(testing, 6)
