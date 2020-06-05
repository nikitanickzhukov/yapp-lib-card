from unittest import TestCase

from card.suit import Suit, suits


class SuitTestCase(TestCase):
    def test_init(self):
        suit = Suit(code='x', name='Suit X')
        with self.assertRaises(AssertionError):
            suit = Suit(code='xx', name='Suit X')
        with self.assertRaises(AssertionError):
            suit = Suit(code='X', name='Suit X')
        with self.assertRaises(AssertionError):
            suit = Suit(code='XX', name='Suit X')
        with self.assertRaises(AssertionError):
            suit = Suit(code='', name='Suit X')
        with self.assertRaises(AssertionError):
            suit = Suit(code='x', name='')

    def test_getters(self):
        suit = Suit(code='x', name='Suit X')
        self.assertEqual(suit.get_code(), 'x')
        self.assertEqual(suit.get_name(), 'Suit X')

    def test_serialize(self):
        suit = suits.get(code='d')
        self.assertEqual(suit.serialize(), 'd')

    def test_deserialize(self):
        suit = Suit.deserialize(code='d')
        self.assertEqual(suit.get_code(), 'd')
        self.assertEqual(suit, suits.get(code='d'))
        self.assertIs(Suit.deserialize(suit.serialize()), suit)

    def test_repo(self):
        suit = suits.get(code='c')
        self.assertEqual(suit.get_code(), 'c')
        self.assertIs(suit, suits.get(code='c'))
        with self.assertRaises(KeyError):
            suit = suits.get(code='a')
