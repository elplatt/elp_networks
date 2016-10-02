from networks import *

class Butterfly(Network):
    
    def __init__(self, m):
        '''Create an m-dimensional butterfly network.'''
        self.nodes = set([(0,0)])
        self.edges = set()
        in_level_max = pow(2, m)
        for level in range(m):
            for in_level in range(in_level_max):
                node = (level, in_level)
                self.nodes.add(node)
                down = ((level + 1) % m, in_level)
                down_right = ((level + 1) % m, in_level ^ (1 << level))
                if node != down:
                    self.edges.add(frozenset((node, down)))
                if node != down_right:
                    self.edges.add(frozenset((node, down_right)))

