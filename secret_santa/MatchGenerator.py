from helper import bipartite_ford_fulkerson
from Edge import Edge
import uuid

class MatchGenerator:
    """
    Class used to generate pairings based on a given list of strings, excluding
    any forbidden pairs.

    Attributes
    ----------
    source_list: list[str]
        List of emails to generate matches for
    forbidden_pairs: dict[str, str]
        Mappings of pairs to exclude, based on email
    sentinel: str
        6 digit randomly generated unique id to append to emails when generating graph.

    Methods
    -------
    generate_graph() -> dict[list[str]]
        Generates a bipartite graph from the provided emails excluding edges in the 
        exclusion list.
    generate_matches() -> None
        Returns a mappings based on source_list.
    """
    sentinel = str(uuid.uuid4())[:6]

    def __init__(self, source_list: list[str], forbidden_pairs: list[str]) -> None:
        """
        Parameters
        ----------
        source_list: list[str]
            List of participants to generate matches for.
        forbidden_pairs: dict[str, str]
            Mappings of pairs to exclude, based on email.
        """
        self.source_list = source_list
        self.forbidden_pairs = forbidden_pairs

    
    def generate_graph(self) -> dict[list[str]]:
        """
        Generates a bipartite graph from the source email list. Prepends a source
        node to the first partition and append a sink node to the second. This transforms
        the graph into a flow network.

        Returns
        -------
        dict[list[str]]
            The flow network used to find mappings
        """
        graph = {
            'source': [],
            'sink': []
        }
        email_list = [x for x in self.source_list]
        email_list_B = [x + self.sentinel for x in email_list]

        for email in email_list:
            e = Edge('source', email, 0, 1)
            rev_e = Edge(email, 'source', 0, 1)
            e.rev, rev_e.rev = rev_e, e
            graph['source'].append(e)
            graph[email] = [rev_e]

        for i in range(len(email_list)):
            candidates = email_list_B[:i] + email_list_B[i+1:]
            email = email_list[i]
            if (email in self.forbidden_pairs):
                for exclusion in self.forbidden_pairs[email]:
                    try:
                        candidates.remove(exclusion + self.sentinel)
                    except ValueError as e:
                        print(e) 
            
            for c in candidates:
                e = Edge(email, c, 0, 1)
                rev_e = Edge(c, email, 0, 1)
                e.rev, rev_e.rev = rev_e, e
                
                if c not in graph:
                    graph[c] = []
                
                graph[email].append(e)
                graph[c].append(rev_e)
        
        for email_B in email_list_B:
            e = Edge(email_B, 'sink', 0, 1)
            rev_e = Edge('sink', email_B, 0, 1)
            e.rev, rev_e.rev = rev_e, e
            graph[email_B].append(e)
            graph['sink'].append(rev_e)

        return graph
    

    def generate_matches(self) -> dict[str, str]:
        """
        Generates pairs based on the source list.

        Returns
        -------
        dict[str, str]
            A dictionary of the generated pairs.
        """
        graph = self.generate_graph()
        bipartite_ford_fulkerson(graph, 'source', 'sink')

        pairings = {}
        for email in self.source_list:
            for e in graph[email]:
                if e.flow == 1:
                    pairings[email] = e.b[:-len(self.sentinel)]
                    break
        

        if len(pairings) < len(self.source_list):
            print("No possible matching exists")
            return {}
        
        return pairings
