from graph.edges import Edge
from typing import Union

class Node:
    def __init__(self, index: int, label=None) -> None:
        """
        Initialize a Node with an index and an optional label.

        :param index: The unique identifier for the node.
        :param label: An optional label for the node.
        """
        self.index: int = index
        self.edges: dict = {}
        self.label = label

    def num_edges(self) -> int:
        """
        Get the number of edges connected to this node.

        :return: The number of edges.
        """
        return len(self.edges)

    def get_edges(self, neighbor: int) -> Union[Edge, None]:
        """
        Retrieve the edge connecting this node to a specified neighbor.

        :param neighbor: The index of the neighbor node.
        :return: The Edge object if it exists, otherwise None.
        """
        if neighbor in self.edges:
            return self.edges[neighbor]
        return None
    
    def add_edge(self, neighbor: int, weight: float):
        """
        Add an edge from this node to a specified neighbor with a given weight.

        :param neighbor: The index of the neighbor node.
        :param weight: The weight of the edge.
        """
        self.edges[neighbor] = Edge(self.index, neighbor, weight)

    def remove_edge(self, neighbor: int):
        """
        Remove the edge connecting this node to a specified neighbor.

        :param neighbor: The index of the neighbor node.
        """
        if neighbor in self.edges:
            del self.edges[neighbor]

    def get_edge_list(self) -> list:
        """
        Get a list of all edges connected to this node.

        :return: A list of Edge objects.
        """
        return list(self.edges.values())
    
    def get_sorted_edge_list(self) -> list:
        """
        Get a sorted list of all edges connected to this node, sorted by neighbor index.

        :return: A list of Edge objects sorted by neighbor index.
        """
        result = []
        neighbors = list(self.edges.keys())
        neighbors.sort()

        for n in neighbors:
            result.append(self.edges[n])
        return result
    