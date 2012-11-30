import sys


class pySV:
    def __init__(self, bamFile):
        self.bamFile = bamFile
        print(self.bamFile)

    def translocation(self):
        pass

    def inversion(self):
        pass

    def deletion(self):
        pass

    def duplication(self):
        pass

sv = pySV(sys.argv[1])
