import unittest
from betweenness import betweenness

weight_from_to = {
    ("A", "B"): 1,
    ("A", "C"): 2,
    ("B", "D"): 2,
    ("C", "D"): 1,
    ("D", "A"): 3,
    ("D", "C"): 1
}

true_dist = {
    'A': {'A':0, 'B':1, 'C':2, 'D':3},
    'B': {'A':5, 'B':0, 'C':3, 'D':2},
    'C': {'A':4, 'B':5, 'C':0, 'D':1},
    'D': {'A':3, 'B':4, 'C':1, 'D':0}
}

true_paths = {
    'A': {'A':[[]], 'B':[[]], 'C':[[]], 'D':[['B'],['C']]},
    'B': {'A':[['D']], 'B':[[]], 'C':[['D']], 'D':[[]]},
    'C': {'A':[['D']], 'B':[['D','A']], 'C':[[]], 'D':[[]]},
    'D': {'A':[[]], 'B':[['A']], 'C':[[]], 'D':[[]]}
}

true_betweenness = {'A':2, 'B':0.5, 'C':0.5, 'D':4}

class TestBetweenness(unittest.TestCase):
    
    def test_betweenness(self):
        b = betweenness(weight_from_to)
        self.assertEqual(b, true_betweenness)

if __name__ == '__main__':
    unittest.main()
    