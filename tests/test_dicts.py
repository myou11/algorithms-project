import unittest
from builtin_types import dicts

class BasicUsage(unittest.TestCase):
    def test_dict_length(self):
        D = dict(zip('python', range(len('python'))))
        n = dicts.dict_length(D)
        self.assertEqual(len(D), n)

    def test_sorted_list_of_items(self):
        D = {'a': 1, 'b': 2}
        l = dicts.sorted_list_of_items(D)
        self.assertEqual(l, sorted(D.items()))

    def test_dict_from_keys_values(self):
        k, v = list('python'), list(range(7, 7 + len('python')))
        D = dicts.dict_from_keys_values(k, v)
        self.assertEqual(D, dict(zip(k, v)))

    def test_update_key(self):
        D = {'a': 1, 'b': 2}
        dicts.update_key(D, 'b', 5)
        self.assertEqual(D['b'], 5)

    def test_remove_key(self):
        D = {'a': 1, 'b': 2}
        dicts.remove_key(D, 'b')
        self.assertNotIn('b', D)

    def test_sorted_list_of_keys(self):
        D = dict(zip('python', range(len('python'))))
        l = dicts.sorted_list_of_keys(D)
        self.assertEqual(l, sorted(D.keys()))


class Challenge(unittest.TestCase):
    def test_inverted_dict(self):
        D = dict(zip('python', range(len('python'))))
        D_inv = dicts.inverted_dict(D)
        self.assertEqual(D_inv, {v: k for k,v in D.items()})
