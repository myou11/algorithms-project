import unittest
from bipartite_recognition.undirected_graph import Graph

def basic_graph1():
    g = Graph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c', {'weight': 7})
    g.add_edge('c', 'd')
    g.add_node('e', {'added': 'Tuesday'})
    return g

class BasicUsage(unittest.TestCase):
    def test_get_edges(self):
        g = basic_graph1()
        edges = set(g.get_edges())
        self.assertIn(('a', 'b'), edges)
        self.assertIn(('b', 'a'), edges)

    def test_neighbors(self):
        g = basic_graph1()
        b_neighbors = set(g.neighbors('b'))
        self.assertIn('a', b_neighbors)
        self.assertIn('c', b_neighbors)

    def test_attributes(self):
        g = basic_graph1()
        att = g.attributes_of('b', 'c')
        self.assertIn('weight', att)
        self.assertEqual(att['weight'], 7)
        self.assertIn('added', g.attributes_of('e'))

    def test_copy(self):
        g = basic_graph1()
        gc = g.copy()
        self.assertEqual(g.edges, gc.edges)
        self.assertEqual(g.nodes, gc.nodes)
        self.assertIsNot(g.edges, gc.edges)
        self.assertIsNot(g.nodes, gc.nodes)
