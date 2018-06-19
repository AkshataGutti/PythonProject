class TextfileReader:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename,'r') as f:
            self.vertice = f.read()
        return self.vertice