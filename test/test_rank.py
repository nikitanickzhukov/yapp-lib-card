from unittest import TestCase

from card.rank import Rank, ranks


class RankTestCase(TestCase):
    def test_init(self):
        rank = Rank(code='A', name='Rank A')
        with self.assertRaises(AssertionError):
            rank = Rank(code='AA', name='Rank A')
        with self.assertRaises(AssertionError):
            rank = Rank(code='a', name='Rank A')
        with self.assertRaises(AssertionError):
            rank = Rank(code='aa', name='Rank A')
        with self.assertRaises(AssertionError):
            rank = Rank(code='', name='Rank A')
        with self.assertRaises(AssertionError):
            rank = Rank(code='A', name='')

    def test_getters(self):
        rank = Rank(code='A', name='Rank A')
        self.assertEqual(rank.get_code(), 'A')
        self.assertEqual(rank.get_name(), 'Rank A')

    def test_serialize(self):
        rank = ranks.get(code='Q')
        self.assertEqual(rank.serialize(), 'Q')

    def test_deserialize(self):
        rank = Rank.deserialize(code='Q')
        self.assertEqual(rank.get_code(), 'Q')
        self.assertEqual(rank, ranks.get(code='Q'))
        self.assertIs(Rank.deserialize(rank.serialize()), rank)

    def test_repo(self):
        rank = ranks.get(code='9')
        self.assertEqual(rank.get_code(), '9')
        self.assertIs(rank, ranks.get(code='9'))
        with self.assertRaises(KeyError):
            rank = ranks.get(code='0')
