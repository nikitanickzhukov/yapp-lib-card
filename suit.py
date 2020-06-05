from __future__ import annotations

from .prop import Prop
from .repo import Repo


class Suit(Prop):
    """
    A card suit (see Prop docs for more information)
    """

    def __init__(self, code: str, name: str) -> None:
        assert len(code) == 1 and 'a' <= code <= 'z', 'code must be a single lowercase char'
        assert len(name) > 0, 'name must not be empty'
        super().__init__(code=code, name=name)

    @classmethod
    def deserialize(cls, code: str) -> Suit:
        return suits.get(code=code)


suits = Repo((
    Suit(code='s', name='spades'),
    Suit(code='h', name='hearts'),
    Suit(code='d', name='diamonds'),
    Suit(code='c', name='clubs'),
))


__all__ = ('Suit', 'suits')
