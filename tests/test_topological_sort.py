import unittest

# Import modules that use local imports
## Adding the folder to the path before
## importing lets the modules being imported
## reference other modules in that same folder
# Goofy, but there are tradeoffs to each approach :/
import sys
folder = 'topological_sort'
sys.path.append(folder)
from topological_sort.core import sort
sys.path.remove(folder)

graph_sample_folder = 'topological_sort/resources/'

def read_edges_from_file(filename):
    '''The file should have lines of the form "x y",
    indicating that there is an edge between the node
    named "x" and the node named "y"'''
    with open(filename) as f:
        return [tuple(line.strip().split()) for line in f.readlines()]

def do_edges_respect_sort(topo_sort, edge_file):
    sort_index = dict(zip(topo_sort, range(len(topo_sort))))
    edges = read_edges_from_file(edge_file)
    for x,y in edges:
        if sort_index[y] < sort_index[x]:
            return False
    return True

class FindSort(unittest.TestCase):
    def test_graph1(self):
        graph_filename = graph_sample_folder + 'graph1.txt'
        topo_sort = sort(graph_filename)
        self.assertTrue(do_edges_respect_sort(topo_sort, graph_filename))

    def test_graph2(self):
        graph_filename = graph_sample_folder + 'graph2.txt'
        topo_sort = sort(graph_filename)
        self.assertTrue(do_edges_respect_sort(topo_sort, graph_filename))

    def test_graph4(self):
        graph_filename = graph_sample_folder + 'graph4.txt'
        topo_sort = sort(graph_filename)
        self.assertTrue(do_edges_respect_sort(topo_sort, graph_filename))

    def test_graph5(self):
        graph_filename = graph_sample_folder + 'graph5.txt'
        topo_sort = sort(graph_filename)
        self.assertTrue(do_edges_respect_sort(topo_sort, graph_filename))

    def test_graph6(self):
        graph_filename = graph_sample_folder + 'graph6.txt'
        topo_sort = sort(graph_filename)
        self.assertTrue(do_edges_respect_sort(topo_sort, graph_filename))

    def test_graph7(self):
        graph_filename = graph_sample_folder + 'graph7.txt'
        topo_sort = sort(graph_filename)
        self.assertTrue(do_edges_respect_sort(topo_sort, graph_filename))

    def test_graph8(self):
        graph_filename = graph_sample_folder + 'graph8.txt'
        topo_sort = sort(graph_filename)
        self.assertTrue(do_edges_respect_sort(topo_sort, graph_filename))

def rotated(l, i):
    return l[i:] + l[:i]

def cycle_equal(c, d):
    '''Given two cycles, where a cycle is a list of
    the nodes in the cycle in order, check that they
    represent the same cycle.
    For example, [1, 2, 3, 4] is equal to [3, 4, 1, 2]'''
    c_front = c[0]
    if c_front not in d:
        return False
    return c == rotated(d, d.index(c_front))

def contains_cycle(cycle, edge_file):
    '''Verify that the graph contains the cycle.
    For example, if cycle = ['x', 'y', 'z'] then graph should have
    edges ('x', 'y') ('y', 'z') and ('z', 'x')'''
    edge_set = set(read_edges_from_file(edge_file))
    cycle_edge_set = set(zip(cycle, rotated(cycle, 1)))
    return cycle_edge_set <= edge_set

class FindCycle(unittest.TestCase):
    def test_graph3(self):
        graph_filename = graph_sample_folder + 'graph3_cycle.txt'
        try:
            topo_sort = sort(graph_filename)
            self.fail('topological sort should have raised an Error!')
        except ValueError as err:
            self.assertTrue(cycle_equal(err.cycle, ['a', 'b', 'c']))

    def test_graph9(self):
        graph_filename = graph_sample_folder + 'graph9_cycle.txt'
        try:
            topo_sort = sort(graph_filename)
            self.fail('topological sort should have raised an Error!')
        except ValueError as err:
            self.assertTrue(cycle_equal(err.cycle, ['a', 'b', 'c', 'd']))

    def test_graph10(self):
        graph_filename = graph_sample_folder + 'graph10_cycle.txt'
        try:
            topo_sort = sort(graph_filename)
            self.fail('topological sort should have raised an Error!')
        except ValueError as err:
            self.assertTrue(cycle_equal(err.cycle, ['h', 'i', 'j', 'k']))

    def test_graph11(self):
        graph_filename = graph_sample_folder + 'graph11_cycle.txt'
        try:
            topo_sort = sort(graph_filename)
            self.fail('topological sort should have raised an Error!')
        except ValueError as err:
            self.assertTrue(cycle_equal(err.cycle, ['H', 'C', 'F', 'I', 'B', 'D']))

    def test_graph12(self):
        graph_filename = graph_sample_folder + 'graph12_cycle.txt'
        try:
            topo_sort = sort(graph_filename)
            self.fail('topological sort should have raised an Error!')
        except ValueError as err:
            self.assertTrue(cycle_equal(err.cycle, ['k', 'm', 'n']))

    def test_graph13(self):
        graph_filename = graph_sample_folder + 'graph13_cycle.txt'
        try:
            topo_sort = sort(graph_filename)
            self.fail('topological sort should have raised an Error!')
        except ValueError as err:
            # there are many cycles in graph13
            # test that the cycle exists
            self.assertTrue(contains_cycle(err.cycle, graph_filename))

    def test_graph14(self):
        graph_filename = graph_sample_folder + 'graph14_cycle.txt'
        try:
            topo_sort = sort(graph_filename)
            self.fail('topological sort should have raised an Error!')
        except ValueError as err:
            # there are many cycles in graph14
            # test that the cycle exists
            self.assertTrue(contains_cycle(err.cycle, graph_filename))
