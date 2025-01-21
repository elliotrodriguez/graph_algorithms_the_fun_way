import unittest
from classes.edges.edge import Edge

class TestEdge(unittest.TestCase):
    
    def test_edge_initialization(self):
        # Create an instance of Edge
        edge = Edge(from_node=1, to_node=2, weight=3.5)
        
        # Test if the attributes are set correctly
        self.assertEqual(edge.from_node, 1)
        self.assertEqual(edge.to_node, 2)
        self.assertEqual(edge.weight, 3.5)

if __name__ == '__main__':
    unittest.main() 