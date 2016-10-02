import elp_networks
import unittest

square_nodes = set(range(4)) 
square_edges = set([
    frozenset((0,1)), frozenset((1,3)), frozenset((3,2)), frozenset((2,0))
])

butterfly_nodes = set([
    (0, 0)
    , (0, 1)
    , (0, 2)
    , (0, 3)
    , (1, 0)
    , (1, 1)
    , (1, 2)
    , (1, 3)
])
butterfly_edges = set([
    frozenset(((0, 0), (1, 0)))
    , frozenset(((0, 0), (1, 1)))
    , frozenset(((0, 1), (1, 0)))
    , frozenset(((0, 1), (1, 1)))
    , frozenset(((0, 2), (1, 2)))
    , frozenset(((0, 2), (1, 3)))
    , frozenset(((0, 3), (1, 2)))
    , frozenset(((0, 3), (1, 3)))
    , frozenset(((0, 3), (1, 1)))
    , frozenset(((0, 1), (1, 3)))
    , frozenset(((0, 0), (1, 2)))
    , frozenset(((0, 2), (1, 0)))
])

nq_two_nodes = set([ (0,0), (1,0), (0,1), (1,1), (0,2), (1,2) ])
nq_two_edges = set([
    frozenset([ (0,0), (1,2) ])
    , frozenset([ (0,0), (1,0) ])
    , frozenset([ (0,1), (1,0) ])
    , frozenset([ (0,1), (1,1) ])
    , frozenset([ (0,2), (1,1) ])
    , frozenset([ (0,2), (1,2) ])    
])

nq_three_nodes = set([
    (0,0,0), (1,0,0), (0,1,0), (1,1,0), (0,2,0), (1,2,0)
    ,(0,0,1), (1,0,1), (0,1,1), (1,1,1), (0,2,1), (1,2,1)
    ,(0,0,2), (1,0,2), (0,1,2), (1,1,2), (0,2,2), (1,2,2)
    ,(0,0,3), (1,0,3), (0,1,3), (1,1,3), (0,2,3), (1,2,3)
    ,(0,0,4), (1,0,4), (0,1,4), (1,1,4), (0,2,4), (1,2,4)
    ,(0,0,5), (1,0,5), (0,1,5), (1,1,5), (0,2,5), (1,2,5)
    ,(0,0,6), (1,0,6), (0,1,6), (1,1,6), (0,2,6), (1,2,6)
])

nq_three_edges = set([
    frozenset([ (0,0,0), (1,0,0) ])
    , frozenset([ (1,0,0), (0,1,0) ])
    , frozenset([ (0,1,0), (1,1,0) ])
    , frozenset([ (1,1,0), (0,2,0) ])
    , frozenset([ (0,2,0), (1,2,0) ])
    , frozenset([ (1,2,0), (0,0,0) ])
    , frozenset([ (0,0,1), (1,0,1) ])
    , frozenset([ (1,0,1), (0,1,1) ])
    , frozenset([ (0,1,1), (1,1,1) ])
    , frozenset([ (1,1,1), (0,2,1) ])
    , frozenset([ (0,2,1), (1,2,1) ])
    , frozenset([ (1,2,1), (0,0,1) ])
    , frozenset([ (0,0,2), (1,0,2) ])
    , frozenset([ (1,0,2), (0,1,2) ])
    , frozenset([ (0,1,2), (1,1,2) ])
    , frozenset([ (1,1,2), (0,2,2) ])
    , frozenset([ (0,2,2), (1,2,2) ])
    , frozenset([ (1,2,2), (0,0,2) ])
    , frozenset([ (0,0,3), (1,0,3) ])
    , frozenset([ (1,0,3), (0,1,3) ])
    , frozenset([ (0,1,3), (1,1,3) ])
    , frozenset([ (1,1,3), (0,2,3) ])
    , frozenset([ (0,2,3), (1,2,3) ])
    , frozenset([ (1,2,3), (0,0,3) ])
    , frozenset([ (0,0,4), (1,0,4) ])
    , frozenset([ (1,0,4), (0,1,4) ])
    , frozenset([ (0,1,4), (1,1,4) ])
    , frozenset([ (1,1,4), (0,2,4) ])
    , frozenset([ (0,2,4), (1,2,4) ])
    , frozenset([ (1,2,4), (0,0,4) ])
    , frozenset([ (0,0,5), (1,0,5) ])
    , frozenset([ (1,0,5), (0,1,5) ])
    , frozenset([ (0,1,5), (1,1,5) ])
    , frozenset([ (1,1,5), (0,2,5) ])
    , frozenset([ (0,2,5), (1,2,5) ])
    , frozenset([ (1,2,5), (0,0,5) ])
    , frozenset([ (0,0,6), (1,0,6) ])
    , frozenset([ (1,0,6), (0,1,6) ])
    , frozenset([ (0,1,6), (1,1,6) ])
    , frozenset([ (1,1,6), (0,2,6) ])
    , frozenset([ (0,2,6), (1,2,6) ])
    , frozenset([ (1,2,6), (0,0,6) ])
    , frozenset([ (1,0,0), (0,1,5) ])
    , frozenset([ (1,1,0), (0,2,3) ])
    , frozenset([ (1,2,0), (0,0,1) ])
    , frozenset([ (1,0,1), (0,1,6) ])
    , frozenset([ (1,1,1), (0,2,4) ])
    , frozenset([ (1,2,1), (0,0,2) ])
    , frozenset([ (1,0,2), (0,1,0) ])
    , frozenset([ (1,1,2), (0,2,5) ])
    , frozenset([ (1,2,2), (0,0,3) ])
    , frozenset([ (1,0,3), (0,1,1) ])
    , frozenset([ (1,1,3), (0,2,6) ])
    , frozenset([ (1,2,3), (0,0,4) ])
    , frozenset([ (1,0,4), (0,1,2) ])
    , frozenset([ (1,1,4), (0,2,0) ])
    , frozenset([ (1,2,4), (0,0,5) ])
    , frozenset([ (1,0,5), (0,1,3) ])
    , frozenset([ (1,1,5), (0,2,1) ])
    , frozenset([ (1,2,5), (0,0,6) ])
    , frozenset([ (1,0,6), (0,1,4) ])
    , frozenset([ (1,1,6), (0,2,2) ])
    , frozenset([ (1,2,6), (0,0,0) ])
])

class TestCube(unittest.TestCase):
    
    def test_base(self):
        cube = elp_networks.Cube(0)
        self.assertEqual(cube.nodes, set((0,)))
        self.assertEqual(cube.edges, set())
        
    def test_square(self):
        cube = elp_networks.Cube(2)
        self.assertEqual(cube.nodes, square_nodes)
        self.assertEqual(cube.edges, square_edges)
        
    def test_iternodes(self):
        nodes = set(elp_networks.Cube.iternodes(2))
        self.assertEqual(nodes, square_nodes)
        
    def test_iterneighbors(self):
        neighbors = set(elp_networks.Cube.iterneighbors(2, 3))
        self.assertEqual(neighbors, set([1,2]))

class TestButterfly(unittest.TestCase):
    
    def test_base(self):
        net = elp_networks.Butterfly(0)
        self.assertEqual(net.nodes, set([(0,0)]))
        self.assertEqual(net.edges, set())

    def test_one(self):
        net = elp_networks.Butterfly(1)
        self.assertEqual(net.nodes, set([(0,0), (0,1)]))
        self.assertEqual(net.edges, set([ frozenset([ (0,0), (0,1) ]) ]))

    def test_two(self):
        net = elp_networks.Butterfly(2)
        self.assertEqual(net.nodes, butterfly_nodes)
        self.assertEqual(net.edges, butterfly_edges)

class TestNestedClique(unittest.TestCase):
    
    def test_N(self):
        net = elp_networks.NestedClique(0)
        self.assertEqual(net._N(4), 1806)
    
    def test_z2v(self):
        z = 0*1 + 2*2 + 3*6
        self.assertEqual(elp_networks.NestedClique._z2v(z, 3), [0, 2, 3])
        
    def test_v2z(self):
        v = (0, 2, 3)
        z =  0*1 + 2*2 + 3*6
        self.assertEqual(elp_networks.NestedClique._v2z(v), z)
    
    def test_base(self):
        net = elp_networks.NestedClique(0)
        self.assertEqual(net.nodes, set([()]))
        self.assertEqual(net.edges, set())
        
    def test_one(self):
        net = elp_networks.NestedClique(1)
        self.assertEqual(net.nodes, set([(0,), (1,)]))
        self.assertEqual(net.edges, set([ frozenset([(0,), (1,)]) ]))
        
    def test_two(self):
        net = elp_networks.NestedClique(2)
        self.assertEqual(net.nodes, nq_two_nodes)
        self.assertEqual(net.edges, nq_two_edges)

    def test_three(self):
        net = elp_networks.NestedClique(3)
        self.assertEqual(net.nodes, nq_three_nodes)
        self.assertEqual(net.edges, nq_three_edges)

if __name__ == '__main__':
    unittest.main()
    