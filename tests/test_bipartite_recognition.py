import unittest

# Import modules that use local imports
## Adding the folder to the path before
## importing lets the modules being imported
## reference other modules in that same folder
# Goofy, but there are tradeoffs to each approach :/
import sys
folder = 'bipartite_recognition'
sys.path.append(folder)
from bipartite_recognition import core as bipart
sys.path.remove(folder)

graph_sample_folder = 'bipartite_recognition/resources/'

class FindColoring(unittest.TestCase):
    def test_graph1(self):
        g = bipart.read_graph_from_file(graph_sample_folder + 'graph1.txt')
        color1, color2 = bipart.bipartite_color_graph(g)
        c1, c2 = {'a', 'c'}, {'b', 'd'}
        if 'a' in color2:
            c1, c2 = c2, c1
        self.assertEqual(c1, color1)
        self.assertEqual(c2, color2)

    def test_graph2(self):
        g = bipart.read_graph_from_file(graph_sample_folder + 'graph2.txt')
        color1, color2 = bipart.bipartite_color_graph(g)
        c1, c2 = {'a', 'e'}, {'b', 'c', 'd'}
        if 'a' in color2:
            c1, c2 = c2, c1
        self.assertEqual(c1, color1)
        self.assertEqual(c2, color2)

    def test_graph2(self):
        g = bipart.read_graph_from_file(graph_sample_folder + 'moebius-kantor-graph.txt')
        color1, color2 = bipart.bipartite_color_graph(g)
        c1 = {'1', '3', '5', '7', '9', '11', '13', '15'}
        c2 = {'2', '4', '6', '8', '10', '12', '14', '16'}
        if '1' in color2:
            c1, c2 = c2, c1
        self.assertEqual(c1, color1)
        self.assertEqual(c2, color2)


def rotated(l, i):
    return l[i:] + l[:i]

def cycle_equal(c, d):
    '''Given two cycles, where a cycle is a list of
    the nodes in the cycle in order, check that they
    represent the same cycle.
    For example, [1, 2, 3, 4] is equal to [3, 4, 1, 2] or
    even [3, 2, 1, 4]'''
    c_front = c[0]
    if c_front not in d:
        return False
    drev = list(reversed(d))
    return (c == rotated(d,       d.index(c_front)) or
            c == rotated(drev, drev.index(c_front)))

def contains_cycle(g, c):
    '''Verify that graph g contains cycle c.
    For example, if c = ['x', 'y', 'z'] then g should have
    edges ('x', 'y') ('y', 'z') and ('z', 'x')'''
    for x, y in zip(c, rotated(c, 1)):
        if y not in g.neighbors(x):
            return False
    return True

class FindOddCycle(unittest.TestCase):
    def test_graph3(self):
        filename = graph_sample_folder + 'graph3_odd_cycle.txt'
        g = bipart.read_graph_from_file(filename)
        try:
            color1, color2 = bipart.bipartite_color_graph(g)
            self.fail('bipartite_color_graph should have raised an Error!')
        except ValueError as err:
            self.assertTrue(cycle_equal(err.odd_cycle, ['a', 'b', 'c']))

    def test_graph4(self):
        filename = graph_sample_folder + 'graph4_odd_cycle.txt'
        g = bipart.read_graph_from_file(filename)
        try:
            color1, color2 = bipart.bipartite_color_graph(g)
            self.fail('bipartite_color_graph should have raised an Error!')
        except ValueError as err:
            # there are many odd cycles in graph4
            # test that the cycle is odd and exists in graph
            self.assertTrue(len(err.odd_cycle) % 2 == 1)
            self.assertTrue(contains_cycle(g, err.odd_cycle))

    def test_moebius_extra_edge(self):
        # http://mathworld.wolfram.com/Moebius-KantorGraph.html
        filename = graph_sample_folder + 'moebius-kantor-graph-extra-edge.txt'
        g = bipart.read_graph_from_file(filename)
        try:
            color1, color2 = bipart.bipartite_color_graph(g)
            self.fail('bipartite_color_graph should have raised an Error!')
        except ValueError as err:
            # there are many odd cycles in moebius-kantor plus extra edge
            # test that the cycle is odd and exists in graph
            self.assertTrue(len(err.odd_cycle) % 2 == 1)
            self.assertTrue(contains_cycle(g, err.odd_cycle))
