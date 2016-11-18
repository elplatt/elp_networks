from networks import *

class Ring(Network):
    
    def __init__(self, n, m=1):
        '''Create an n-node clique with connections to 2m nearest neighbors.'''
        self.m = m
        self.n = n
        # Create nodes
        self.nodes = set(range(0,n))
        # Create edges
        self.edges = set()
        for v in self.nodes:
            for delta in range(1,m+1):
                w = delta % n
                self.edges.add(frozenset((v, w)))
    
    @classmethod
    def iternodes(cls, n, m=1):
        return xrange(n)
    
    @classmethod
    def iterneighbors(cls, n, m, v):
        for delta in xrange(1,m+1):
            yield (v - delta) % n
            yield (v + delta) % n
    
    def neighbors(self, v):
        return Ring.iterneighbors(self.n, self.m, v)
    
    @classmethod
    def pathlength_counts(cls, m):
        raise NotImplementedError

