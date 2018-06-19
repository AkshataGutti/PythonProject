from vertex import Vertex
from graph import Graph
def shortest( v, path):
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
        return  