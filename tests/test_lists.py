import unittest
from builtin_types import lists

class BasicUsage(unittest.TestCase):
    def test_list_of_range(self):
        L = lists.list_of_range(0, 5)
        self.assertEqual(L, list(range(5)))

        L = lists.list_of_range(5, 12)
        self.assertEqual(L, list(range(5, 12)))

    def test_list_of_chars(self):
        L = lists.list_of_chars("hello")
        self.assertEqual(L, ['h', 'e', 'l', 'l', 'o'])

    def test_list_extend(self):
        L = list(range(5))
        lists.list_extend(L, range(5, 8))
        self.assertEqual(L, list(range(8)))

    def test_list_length(self):
        for i in range(10, 20):
            with self.subTest(length=i):
                L = list(range(i))
                self.assertEqual(i, lists.list_length(L))

    def test_get_item_at(self):
        for i in range(10):
            with self.subTest(item_position=i):
                L = list(reversed(range(10)))
                self.assertEqual(9 - i, lists.get_item_at(L, i))
        
    def test_get_second_to_last_item(self):
        L = list(range(20))
        self.assertEqual(18, lists.get_second_to_last_item(L))

    def test_slice_from_to(self):
        L = list('Hello, world!')
        self.assertEqual(L[2:5], lists.slice_from_to(L, 2, 5))

    def test_slice_last_n(self):
        a = 'Hello, world!'
        for i in range(len(a) + 1):
            with self.subTest(n=i):
                L = list(a)
                self.assertEqual(L[-i:], lists.slice_last_n(L, i))

    def test_copy_of_list(self):
        for i in range(4):
            with self.subTest(i=i):
                L = list(range(i))
                C = lists.copy_of_list(L)
                self.assertEqual(L, C)
                self.assertIsNot(L, C)

    def test_slice_every_third_element(self):
        for i in range(20):
            with self.subTest(length=i):
                L = list(range(i))
                S = lists.slice_every_third_element(L)
                self.assertEqual(L[::3], S)

    def test_square_each(self):
        self.assertEqual([0, 1, 4, 9, 16], lists.square_each(list(range(5))))

    def test_if_even_square_each(self):
        self.assertEqual([0, 4, 16], lists.if_even_square_each(list(range(5))))


class Challenge(unittest.TestCase):
    def test_most_frequent_element(self):
        self.assertEqual(lists.most_frequent_element(list('hello')), 'l')
        self.assertEqual(lists.most_frequent_element(list('3.1415926535897932384626433832')), '3')

    def test_positive_number_count(self):
        self.assertEqual(5, lists.positive_number_count([3, 2, -1, -3,
                                                         5, 2, -5, 1]))
