import sys
from collections import deque
from undirected_graph import Graph

def read_edges_from_file(filename):
    with open(filename) as f:
        return [tuple(line.strip().split()) for line in f.readlines()]

def read_graph_from_file(filename):
    edges = read_edges_from_file(filename)
    g = Graph()
    for v, u in edges:
        g.add_edge(v, u)
    return g

def parent_path(g, n):
    ret = []
    while n != None:
        ret.append(n)
        n = g.attributes_of(n)['parent']
    return ret

def lowest_common_ancestor(g, a, b):
    a_ancestors = set(parent_path(g, a))
    for b_ancestor in parent_path(g, b):
        if b_ancestor in a_ancestors:
            return b_ancestor
    x = '{} and {} are not part of the same parent tree'
    raise ValueError(x.format(a, b))

def odd_cycle_helper(g, a, b):
    lca = lowest_common_ancestor(g, a, b)
    app = parent_path(g, a)
    app = app[: app.index(lca) + 1]
    bpp = parent_path(g, b)
    bpp = bpp[: bpp.index(lca) + 1]
    return list(reversed(app)) + bpp[:-1]

def bipartite_color_graph(g):
    '''Assumes g is connected, otherwise run on each
    component and assemble final coloring from component coloring'''
    g = g.copy()
    s = list(g.nodes)[0]
    g.attributes_of(s).update({'color': 0, 'parent': None})
    q = deque([s])
    while(len(q) > 0):
        n = q.popleft()
        ncolor = g.attributes_of(n)['color']
        for neighbor in g.neighbors(n):
            neighbor_attr = g.attributes_of(neighbor)
            if 'parent' in neighbor_attr:
                if neighbor_attr['color'] != 1 - ncolor:
                    odd_cycle_nodes = odd_cycle_helper(g, n, neighbor)
                    x = 'Not bipartite. Odd cycle in graph: {}'
                    raise ValueError(x.format(odd_cycle_nodes))
            else:
                q.append(neighbor)
                neighbor_attr.update({'color': 1 - ncolor,
                                          'parent': n})

    ret_lists = ([], [])
    for node in g.nodes:
        color = g.attributes_of(node)['color']
        ret_lists[color].append(node)
    return ret_lists

def main(argv):
    g = read_graph_from_file(argv[1])
    print(bipartite_color_graph(g))

if __name__ == "__main__":
    main(sys.argv)
