import unittest
from classes.graphs.graph import Graph
from classes.edges.edge import Edge

class TestGraph(unittest.TestCase):
    
    def test_graph_initialization(self):
        # Create an instance of Graph
        graph = Graph(num_nodes=3, undirected=True)
        
        # Test if the attributes are set correctly
        self.assertEqual(graph.num_nodes, 3)
        self.assertTrue(graph.undirected)
        self.assertEqual(len(graph.nodes), 3)

    def test_insert_edge(self):
        graph = Graph(num_nodes=3)
        graph.insert_edge(from_node=0, to_node=1, weight=2.5)
        
        # Test if the edge is added correctly
        edge = graph.get_edge(0, 1)
        self.assertIsNotNone(edge)
        self.assertEqual(edge.from_node, 0)
        self.assertEqual(edge.to_node, 1)
        self.assertEqual(edge.weight, 2.5)

    def test_remove_edge(self):
        graph = Graph(num_nodes=3)
        graph.insert_edge(from_node=0, to_node=1, weight=2.5)
        graph.remove_edge(from_node=0, to_node=1)
        
        # Test if the edge is removed correctly
        self.assertIsNone(graph.get_edge(0, 1))

    def test_is_edge(self):
        graph = Graph(num_nodes=3)
        graph.insert_edge(from_node=0, to_node=1, weight=2.5)
        
        # Test if the edge exists
        self.assertTrue(graph.is_edge(0, 1))
        self.assertFalse(graph.is_edge(1, 2))

    def test_make_edge_list(self):
        graph = Graph(num_nodes=3)
        graph.insert_edge(from_node=0, to_node=1, weight=2.5)
        graph.insert_edge(from_node=1, to_node=2, weight=3.5)
        
        # Test if the edge list is correct
        edge_list = graph.make_edge_list()
        self.assertEqual(len(edge_list), 2)
        self.assertTrue(all(isinstance(edge, Edge) for edge in edge_list))

    def test_insert_node(self):
        graph = Graph(num_nodes=3)
        new_node = graph.insert_node(label="New Node")
        
        # Test if the node is added correctly
        self.assertEqual(graph.num_nodes, 4)
        self.assertEqual(new_node.label, "New Node")

    def test_make_copy(self):
        graph = Graph(num_nodes=3, undirected=True)
        graph.insert_edge(from_node=0, to_node=1, weight=2.5)
        graph.insert_edge(from_node=1, to_node=2, weight=3.5)
        
        # Make a copy of the graph
        graph_copy = graph.make_copy()
        
        # Test if the copy is correct
        self.assertEqual(graph_copy.num_nodes, graph.num_nodes)
        self.assertTrue(graph_copy.undirected)
        self.assertEqual(len(graph_copy.make_edge_list()), len(graph.make_edge_list()))

if __name__ == '__main__':
    unittest.main() 