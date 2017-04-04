import unittest
from builtin_types import sets

class BasicUsage(unittest.TestCase):
    def test_create_set_from_elements(self):
        L = 'python'
        S = sets.create_set_from_elements(L)
        self.assertEqual(S, set(L))

    def test_union_sets(self):
        A, B = set('python'), set('the')
        U = sets.union_sets(A, B)
        self.assertEqual(U, set('pythonthe'))

    def test_key_in_set(self):
        A = set('python')
        self.assertTrue(sets.key_in_set(A, 'p'))
        self.assertFalse(sets.key_in_set(A, 'x'))
