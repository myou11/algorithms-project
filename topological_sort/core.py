import sys
from collections import deque
from directed_graph import Digraph

# Feel free to use bipartite_recognition/core.py as a reference

def read_edges_from_file(filename):
    with open(filename) as f:
        return [tuple(line.strip().split()) for line in f.readlines()]

def read_graph_from_file(filename):
    edges = read_edges_from_file(filename)  # returns a list of edges as tuples
    g = Digraph()             # create a graph to return
    for v, u in edges:      # for each edge(tuple) in the edge list
        g.add_edge(v, u)    # add the edges to the graph
    return g                #return the graph

def cycleFinder(graph, u, v):
    cycle = [u]                                 # we know the cycle will contain u, since u was about
                                                # to search vertex v which would have formed a cycle
    parent = graph.attributes_of(u)['parent']   # set parent to the parent of u
    
    # follow parent ptrs until you get back to u
    while parent != v:          # while the parent ptrs are not the vertex that would have created a cycle
        cycle.append(parent)    # add the nodes that are in the cycle
        parent = graph.attributes_of(parent)['parent']  # the new parent is the parent of the current parent

    cycle.append(v)     # add in the vertex that would have formed a cycle

    return list(reversed(cycle))        # reverse the list because we followed parent ptrs,
                                        # which went in the opposite direction of the cycle

def dfs(graph):
    graph = graph.copy()    # copy the graph so we don't modify the original
    dfsOrder = deque([])    # create a list to store the result of DFS

    # init the color and parent of every node in the graph to be white and None, respectively
    for u in graph.nodes:
        graph.attributes_of(u).update({'color': 0, 'parent': None}) 
    
    # visit all vertices until all "blackened"
    for u in graph.nodes:
        nodeColor = graph.attributes_of(u)['color'] # get color of current vertex u
        if nodeColor == 0:                          # if u's color is white
            dfs_visit(graph, u, dfsOrder)           # search vertex u depth-first(recursively)
    
    return dfsOrder     # return the dfs order of searching

def dfs_visit(graph, u, dfsOrder):
    graph.attributes_of(u)['color'] = 1             # gray u (mark as discovered)
    for v in graph.edges[u]:                        # for each vertex v in the adjList[u]

        if graph.attributes_of(v)['color'] == 0:    # if v's color is white
            graph.attributes_of(v)['parent'] = u    # change the parent of v to u
            dfs_visit(graph, v, dfsOrder)           # visit vertex v depth-first(recursively)

        if graph.attributes_of(v)['color'] == 1:
            err = ValueError("There's a cycle here!")   # create a ValueError obj
            err.cycle = cycleFinder(graph, u, v)        # attach list of cycles to err obj
            raise err                                   # raise the error
    graph.attributes_of(u)['color'] = 2                 # blacken u (mark as visited)
    dfsOrder.append(u)                                  # add u to result list

def sort(directed_graph_filename):
    '''Given a file containing the edges of a directed graph,
    compute a topological sort of the nodes, returning them as a list.
    If the input graph is not a DAG, raise a ValueError with the nodes
    of cycle attached as a list, in cycle order.'''
    #  read in graph from file
    g = read_graph_from_file(directed_graph_filename)

    #  compute a topological sort using DFS
    dfsResult = list(dfs(g))    # convert the returned deque into a list because can't easily slice a deque
    topoSort = dfsResult[::-1]  # slice the whole list (basically copy it), with a step of -1 (reverse)
    
    #  return the sort as a list of nodes, like:
    #  return ['a', 'b', 'c']
    return topoSort
    
    #  unless you detect a cycle. If there is a cycle,
    #  there is no way to topologically sort the nodes.
    #  so create a ValueError object, like this:
    #  err = ValueError("There's a cycle in here!")
    #  then attach a list of the nodes in the cycle, like this:
    #  err.cycle = ['a', 'b', 'c']
    #  and raise the error, like this:
    #  raise err


# For example, the file topological_sort/resources/graph1.txt looks like:
# a b
# b c
# c d
# And represents a graph like: a->b->c->d
# The function would return the topological sort as ['a', 'b', 'c', 'd']

# However, the file topological_sort/resources/graph3_cycle.txt looks like:
# a b
# b c
# c a
# And represents a graph like: a->b->c
#                              ^-----|
# It's a cycle of size three. The function would raise a ValueError.
# The error object would have a field, cycle, holding the nodes of the cycle.
# The cycle should be ['a', 'b', 'c'] or ['b', 'c', 'a'] or ['c', 'a', 'b']

def main(argv):
    '''An example main to make it easy to try from the command line'''
    if len(argv) < 2:
        print('Must provide a filename for the graph to work on.')
        exit(1)
    graph_filename = argv[1]
    try:
        topo_sort = sort(graph_filename)
        print('Graph is a DAG. It\'s topological sort is:')
        print(topo_sort)
    except ValueError as err:
        print('Graph contains a cycle, cannot perform a topological sort.')
        print('The cycle is: {}'.format(err.cycle))

if __name__ == "__main__":
    main(sys.argv)
