from __future__ import annotations
from abc import ABC, abstractmethod


class Prop(ABC):
    """
    An abstract card property

    Parameters
    ----------
        code : str
            A code
        name : str
            A name

    Methods
    -------
        __str__()
        __repr__()
        __hash__()
        get_code() : str
            Returns a code
        get_name() : str
            Returns a name
    """

    __slots__ = ('_code', '_name')

    def __init__(self, code: str, name: str) -> None:
        self._code = code
        self._name = name

    def __str__(self) -> str:
        return self._code

    def __repr__(self) -> str:
        return '<{}: {}>'.format(self.__class__.__name__, self._name)

    def __hash__(self) -> int:
        return hash(self._code)

    def get_code(self) -> str:
        return self._code

    def get_name(self) -> str:
        return self._name

    def serialize(self) -> str:
        return self.get_code()

    @classmethod
    @abstractmethod
    def deserialize(cls, code: str) -> Prop:
        pass


__all__ = ('Prop',)
