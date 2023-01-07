from __future__ import annotations

from typing import TypeVar, TYPE_CHECKING


if TYPE_CHECKING:
    from typing import Any, Type


T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)


def ensure_type(value: Any, cls: Type[T]) -> T:
    if type(value) == cls:
        return value

    raise ValueError(value)
