import xml.etree.ElementTree as ET


class XMLReader:

    def __init__(self, roadsegment):
        self.roadsegment = roadsegment

    def read(self):
        tree = ET.parse(self.roadsegment)
        self.root = tree.getroot()

    def get_edges(self):
        edges = []
        for route in self.root.findall('route'):
            edges.append(route.find('origin').text+'-'
                         + route.find('destination').text + '-'
                         + route.find('distance').text + '-'
                         + route.find('roadsegment').text)
        return edges
    def get_time_duration(self, source, destn):
        for route in self.root.findall('route'):
            if (source == route.find('origin').text
                    and destn == route.find('destination').text):
                speed = float(route.find('speed').text)
                distance = float(route.find('distance').text)
                time = (distance/speed)
                return time, distance
            elif (source == route.find('destination').text
                    and destn == route.find('origin').text):
                speed = float(route.find('speed').text)
                distance = float(route.find('distance').text)
                time = (distance/speed)
                return time, distance