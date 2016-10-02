from networks import *

class NestedClique(Network):
    
    def __init__(self, m):
        '''Create an m-dimensional nested clique.'''
        N = NestedClique._N(m)
        self.nodes = set()
        self.edges = set()
        for z in range(N):
            v = NestedClique._z2v(z, m)
            self.nodes.add(tuple(v))
            # Only add edges for odd nodes to prevent double counting
            if z % 2 == 1:
                for w in NestedClique.neighbors(v):
                    self.edges.add(frozenset( (tuple(v), w) ))
    
    @classmethod
    def path_length_histogram(cls, m):
        surface = set([tuple([0] * m)])
        last_surface = set([])
        dist = []
        count = []
        surface_dist = 0
        while len(surface) > 0:
            dist.append(surface_dist)
            count.append(len(surface))
            next_surface = set()
            for v in surface:
                for w in cls.neighbors(v):
                    if (w not in last_surface
                            and w not in surface):
                        next_surface.add(w)
            last_surface = surface
            surface = next_surface
            surface_dist += 1
        return (dist, count)
        
    
    @classmethod
    def neighbors(cls, v):
        '''Returns an iterator of the neighbors of a given node.'''
        # See paper notebook ELP-UM-001 p.51
        m = len(v)
        z = cls._v2z(v)
        w = list(v)
        zz = 0
        # Create level-k edges by changing lowest k values
        for i in range(m):
            Ni = NestedClique._N(i)
            if z % 2 == 1:
                w[i] = (w[i] - 1 - zz) % (Ni + 1)
                zz += Ni * v[i]
            else:
                w[i] = (w[i] + 1 + zz ) % (Ni + 1)
                zz += Ni * w[i]
            yield tuple(w)
    
    @classmethod
    def _v2z(cls, v):
        '''Convert from vertex to integer.'''
        z = 0
        for (i, vi) in enumerate(v):
            z += cls._N(i) * vi
        return z
    
    @classmethod
    def _z2v(cls, z, m):
        '''Convert from integer to vertex.'''
        i = 0
        v = []
        zz = z
        while zz > 0 or i < m:
            N = cls._N(i)
            nextN = cls._N(i + 1)
            remainder = zz % nextN
            zz -= remainder
            v.append(int(remainder/N))
            i += 1
        return v
    
    @classmethod
    def _N(cls, i):
        try:
            return cls._N_cache[i]
        except AttributeError:
            cls._N_cache = [1]
        except IndexError:
            pass
        last = cls._N(i - 1)
        result = last * (last + 1)
        cls._N_cache.append(result)
        return result
 