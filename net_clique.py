from networks import *

class Clique(Network):
    
    def __init__(self, m):
        '''Create an m-node clique.'''
        self.m = m
        # Create nodes
        self.nodes = set(range(0,m))
        # Create edges
        self.edges = set()
        for v in self.nodes:
            for w in self.nodes:
                if w >= v:
                    break
                self.edges.add(frozenset((v, w)))
    
    @classmethod
    def iternodes(cls, m):
        return xrange(m)
    
    @classmethod
    def iterneighbors(cls, m, v):
        for w in xrange(m):
            if w == v:
                continue
            yield w
    
    def neighbors(self, v):
        return Clique.iterneighbors(self.m, v)
    
    @classmethod
    def pathlength_counts(cls, m):
        raise NotImplementedError

