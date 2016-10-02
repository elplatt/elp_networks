import math
from networks import *

class Cube(Network):
    
    def __init__(self, m):
        '''Create an m-dimensional cube.'''
        # Create nodes
        self.nodes = set(range(0,pow(2,m)))
        # Create edges
        self.edges = set()
        basis = [pow(2, i) for i in range(m)]
        for node in self.nodes:
            # Add an edge for each bit, but only to nodes with higher ids
            # to avoid double counting.
            for i in xrange(m):
                bit = basis[i]
                if node & bit == 0:
                    self.edges.add(frozenset((node, node | bit)))
    
    @classmethod
    def iternodes(cls, m):
        return xrange(pow(2,m))
    
    @classmethod
    def iterneighbors(cls, m, v):
        for i in xrange(m):
            yield v ^ (1 << i)
    
    @classmethod
    def pathlength_counts(cls, m):
        lengths = range(m + 1)
        counts = [math.factorial(m) / math.factorial(h) / math.factorial(m-h) for h in lengths]
        return (lengths, counts)

