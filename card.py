from __future__ import annotations

from .rank import Rank, ranks
from .suit import Suit, suits
from .repo import Repo


class Card:
    """
    A card

    Parameters
    ----------
        rank : Rank
            A card rank
        suit : Suit
            A card suit

    Methods
    -------
        __str__()
        __repr__()
        __hash__()
        get_rank() : Rank
            Returns a card rank
        get_suit() : Suit
            Returns a card suit
        get_code() : str
            Returns a card code
        get_name() : str
            Returns a card name
    """

    __slots__ = ('_rank', '_suit')

    def __init__(self, rank: Rank, suit: Suit) -> None:
        self._rank = rank
        self._suit = suit

    def __str__(self) -> str:
        return self.get_code()

    def __repr__(self) -> str:
        return '<{}: {}>'.format(self.__class__.__name__, self.get_name())

    def __hash__(self) -> int:
        return hash(self.get_code())

    def get_rank(self) -> Rank:
        return self._rank

    def get_suit(self) -> Suit:
        return self._suit

    def get_code(self) -> str:
        return self._rank.get_code() + self._suit.get_code()

    def get_name(self) -> str:
        return '{} of {}'.format(self._rank.get_name(), self._suit.get_name())

    def serialize(self) -> str:
        return self.get_code()

    @classmethod
    def deserialize(cls, code: str) -> Card:
        return cards.get(code=code)


cards = Repo(
    Card(rank=r, suit=s) for s in suits for r in ranks
)


__all__ = ('Card', 'cards')
