from typing import Sequence, Any, Tuple


class Repo(tuple):
    """
    A repository for storing and searching instances

    Parameters
    ----------
        The same as in tuple

    Methods
    -------
        The same as in tuple
        get() : str
            Returns a single item by code
        get_many() : str
            Returns multiple items by codes
    """

    def __init__(self, *args, **kwargs) -> None:
        self._idx = {x.get_code(): i for i, x in enumerate(self)}

    def get(self, code: str) -> Any:
        return self[self._idx[code]]

    def get_many(self, codes: Sequence[str]) -> Tuple[Any]:
        return tuple(self.get(code=x) for x in codes)


__all__ = ('Repo',)
