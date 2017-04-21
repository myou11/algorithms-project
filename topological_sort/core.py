import sys
#from directed_graph import Digraph

# Feel free to use bipartite_recognition/core.py as a reference


def sort(directed_graph_filename):
    '''Given a file containing the edges of a directed graph,
    compute a topological sort of the nodes, returning them as a list.
    If the input graph is not a DAG, raise a ValueError with the nodes
    of cycle attached as a list, in cycle order.'''
    #  read in graph from file
    #  compute a topological sort using DFS
    #  return the sort as a list of nodes, like:
    return ['a', 'b', 'c']
    #  unless you detect a cycle. If there is a cycle,
    #  there is no way to topologically sort the nodes.
    #  so create a ValueError object, like this:
    # err = ValueError("There's a cycle in here!")
    #  then attach a list of the nodes in the cycle, like this:
    # err.cycle = ['a', 'b', 'c']
    #  and raise the error, like this:
    # raise err


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
