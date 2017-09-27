import unittest
from shortest_paths import floyd_warshall

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
    'A': {'A':[['A']], 'B':[['A','B']], 'C':[['A','C']], 'D':[['A','B','D'],['A','C','D']]},
    'B': {'A':[['B','D','A']], 'B':[['B']], 'C':[['B','D','C']], 'D':[['B','D']]},
    'C': {'A':[['C','D','A']], 'B':[['C','D','A','B']], 'C':[['C']], 'D':[['C','D']]},
    'D': {'A':[['D','A']], 'B':[['D','A','B']], 'C':[['D','C']], 'D':[['D']]}
}

class TestFloydWarshall(unittest.TestCase):
    
    def test_paths(self):
        dist, paths = floyd_warshall(weight_from_to)
        self.assertEqual(dist, true_dist)
        self.assertEqual(paths, true_paths)

if __name__ == '__main__':
    unittest.main()
    