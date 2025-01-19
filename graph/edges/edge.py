class Edge:
    def __init__(self, from_node: int, to_node: int, weight: float) -> None:
        self.from_node: int = from_node
        self.to_node: int = to_node
        self.weight: float = weight