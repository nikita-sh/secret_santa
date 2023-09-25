from collections import deque
import random
from Edge import Edge

def get_path(pred: dict[str, str], src: str, tgt: str) -> list[Edge]:
    """
    Retrieves the path from node src to node tgt in some graph
    using the provided predecessor mapping pred.

    Parameters
    ----------
    pred: dict[str, str]
        A mapping of predecessors representing how a graph was
        traversed to reach tgt from src.
    src: str
        The source node used in the search that created pred.
    tgt: str
        The target node in the search that created pred.

    Returns
    -------
    list[Edge]
        A list of edges representing the path used to reach tgt from src.
    """
    path = []
    curr = tgt
    while curr != src:
        path.append(pred[curr])
        curr = pred[curr].a
    return path[::-1]


def bfs(graph: dict[str, str], src: str, tgt: str) -> list[Edge]:
    """
    Runs Breadth-First-Search on the provided graph from node src searching
    for node tgt and returns the path used to reach it (if one exists).

    Parameters
    ----------
    graph: dict[str, str]
        An adjacency list representing the graph being searched.
    src: str
        The source node the search originates from.
    tgt: str
        The node that is being searched for.


    Returns
    -------
    list[Edge]
        The path used to traverse from src to tgt or an empty
        list if no such path exists.
    """
    queue = deque([src])
    pred = {}

    while queue:
        curr = queue.popleft()
        random.shuffle(graph[curr])
        for neighbor in graph[curr]:
            if neighbor.b == tgt and neighbor.flow < neighbor.capacity:
                pred[neighbor.b] = neighbor
                return get_path(pred, src, tgt)
            elif neighbor.b not in pred and neighbor.b != 'source' and neighbor.flow < neighbor.capacity:
                pred[neighbor.b] = neighbor
                queue.append(neighbor.b)
    
    return []


def bipartite_ford_fulkerson(graph: dict[str, str], source: str, sink: str) -> None:
    """
    Runs the Ford-Fulkerson algorithm on a bipartite graph and
    returns the mappings based on which edge was used to add
    flow in every iteration.

    Parameters
    ----------
    graph: dict[str, str]
        A graph that mappings will be generated for. This function expects
        this graph to be a valid directed, bipartite graph with appended source and
        sink nodes.
    source: str
        The source node from which flow originates.
    sink: str
        The sink node to which flow is directed.
    """
    while True:
        path = bfs(graph, source, sink)
        if not path:
            break
        
        df = min([x.capacity - x.flow for x in path])
        for e in path:
            e.flow += df
            e.rev.flow -= df
        
