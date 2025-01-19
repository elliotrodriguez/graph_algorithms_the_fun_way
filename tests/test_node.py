import unittest
from graph.nodes.nodes import Node
from graph.edges.edge import Edge

class TestNode(unittest.TestCase):
    
    def test_node_initialization(self):
        # Create an instance of Node
        node = Node(index=1, label="A")
        
        # Test if the attributes are set correctly
        self.assertEqual(node.index, 1)
        self.assertEqual(node.label, "A")
        self.assertEqual(node.num_edges(), 0)

    def test_add_edge(self):
        node = Node(index=1)
        node.add_edge(neighbor=2, weight=3.5)
        
        # Test if the edge is added correctly
        edge = node.get_edges(2)
        self.assertIsNotNone(edge)
        self.assertEqual(edge.from_node, 1)
        self.assertEqual(edge.to_node, 2)
        self.assertEqual(edge.weight, 3.5)

    def test_remove_edge(self):
        node = Node(index=1)
        node.add_edge(neighbor=2, weight=3.5)
        node.remove_edge(neighbor=2)
        
        # Test if the edge is removed correctly
        self.assertIsNone(node.get_edges(2))
        self.assertEqual(node.num_edges(), 0)

    def test_get_edge_list(self):
        node = Node(index=1)
        node.add_edge(neighbor=2, weight=3.5)
        node.add_edge(neighbor=3, weight=2.5)
        
        # Test if the edge list is correct
        edge_list = node.get_edge_list()
        self.assertEqual(len(edge_list), 2)
        self.assertTrue(all(isinstance(edge, Edge) for edge in edge_list))

    def test_get_sorted_edge_list(self):
        node = Node(index=1)
        node.add_edge(neighbor=3, weight=2.5)
        node.add_edge(neighbor=2, weight=3.5)
        
        # Test if the sorted edge list is correct
        sorted_edge_list = node.get_sorted_edge_list()
        self.assertEqual(len(sorted_edge_list), 2)
        self.assertEqual(sorted_edge_list[0].to_node, 2)
        self.assertEqual(sorted_edge_list[1].to_node, 3)

if __name__ == '__main__':
    unittest.main() 