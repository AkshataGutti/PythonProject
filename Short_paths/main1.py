from XmlfileReader import XMLReader
from TextfileReader import TextfileReader
from graph import Graph
from Dijkstra import dijkstra
from shortest import shortest
import sys
class FindShortestpath: 
    def read_graphs(self, source, destination, textFileRead, xmlFileRead):
        vertexReader = TextfileReader(textFileRead)
        xmlread = XMLReader(xmlFileRead)
        trace = Graph()
        xmlread.read()
        nodes = vertexReader.read()
        print 'Text File Data:',nodes
        edges = xmlread.get_edges()
        print 'XML file Data:',edges
        for n in nodes: 
            trace.add_vertex(n)
        for e in edges:
            segment = e.split('-')
            trace.add_edge(segment[0], segment[1], int(segment[2]))
        print '\nGraph data:'
        for v in trace:
            for w in v.get_connections():
                vid = v.get_id()
                wid = w.get_id()
                print '( %s, %s, %3d)' % (vid, wid, v.get_weight(w))
        dijkstra(trace, trace.get_vertex(source),trace.get_vertex(destination))
        target = trace.get_vertex(destination)  
        path = [target.get_id()]
        shortest(target, path)
        print '\nThe shortest path : %s' %(path[::-1])
if __name__=='__main__':
    source= sys.argv[1]
    destination = sys.argv[2]
    textFileRead = sys.argv[3]
    xmlFileRead = sys.argv[4]
    read = FindShortestpath()
    read.read_graphs(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])