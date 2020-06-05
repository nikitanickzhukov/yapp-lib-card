from unittest import TestCase

from card.rank import Rank
from card.suit import Suit
from card.card import Card, cards


class CardTestCase(TestCase):
    def test_init(self):
        rank = Rank(code='A', name='Rank A')
        suit = Suit(code='x', name='Suit X')
        card = Card(rank=rank, suit=suit)

    def test_getters(self):
        rank = Rank(code='A', name='Rank A')
        suit = Suit(code='x', name='Suit X')
        card = Card(rank=rank, suit=suit)
        self.assertEqual(card.get_code(), 'Ax')
        self.assertEqual(card.get_name(), 'Rank A of Suit X')

    def test_serialize(self):
        card = cards.get(code='Qd')
        self.assertEqual(card.serialize(), 'Qd')

    def test_deserialize(self):
        card = Card.deserialize(code='Qd')
        self.assertEqual(card.get_code(), 'Qd')
        self.assertEqual(card, cards.get(code='Qd'))
        self.assertIs(Card.deserialize(card.serialize()), card)

    def test_repo(self):
        card = cards.get(code='9c')
        self.assertEqual(card.get_code(), '9c')
        self.assertIs(card, cards.get(code='9c'))
        with self.assertRaises(KeyError):
            card = cards.get(code='Ax')
