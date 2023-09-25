class Edge:
    """
    Container class to represent a directed edge

    Attributes
    ----------
    a: Edge
        The source edge
    b: Edge
        The destination edge
    flow: int
        The flow being carried by this edge.
    capacity: int
        The capacity of this edge.
    rev: Edge
        A pointer to the reverse of this edge.
    """
    def __init__(self, a, b, flow, capacity):
        self.a, self.b = a, b 
        self.flow, self.capacity = flow, capacity
    