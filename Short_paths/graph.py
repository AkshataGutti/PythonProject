
import logging
from vertex import Vertex


class Graph:

    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        logging.basicConfig(filename='logfile', format='%(levelname)s %(asctime)s \
            %(message)s', level=logging.DEBUG)
        logging.debug('Vertices are added')
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, from_, to, cost=0):
        if from_ not in self.vert_dict:
            self.add_vertex(from_)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[from_].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[from_], cost)
        logging.basicConfig(filename='logfile', format='%(levelname)s %(asctime)s \
            %(message)s', level=logging.DEBUG)
        logging.debug('edges are added')

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

    def shortest(self, v, path):
        ''' make shortest path from v.previous'''
        if v.previous:
            path.append(v.previous.get_id())
            self.shortest(v.previous, path)
            return


