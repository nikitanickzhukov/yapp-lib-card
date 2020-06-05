from __future__ import annotations

from .prop import Prop
from .repo import Repo


class Rank(Prop):
    """
    A card rank (see Prop docs for more information)
    """

    def __init__(self, code: str, name: str) -> None:
        assert len(code) == 1 and ('A' <= code <= 'Z' or '0' <= code <= '9'), 'code must be a single uppercase char'
        assert len(name) > 0, 'name must not be empty'
        super().__init__(code=code, name=name)

    @classmethod
    def deserialize(cls, code: str) -> Rank:
        return ranks.get(code=code)


ranks = Repo((
    Rank(code='A', name='ace'),
    Rank(code='2', name='deuce'),
    Rank(code='3', name='trey'),
    Rank(code='4', name='four'),
    Rank(code='5', name='five'),
    Rank(code='6', name='six'),
    Rank(code='7', name='seven'),
    Rank(code='8', name='eight'),
    Rank(code='9', name='nine'),
    Rank(code='T', name='ten'),
    Rank(code='J', name='jack'),
    Rank(code='Q', name='queen'),
    Rank(code='K', name='king'),
))


__all__ = ('Rank', 'ranks')
