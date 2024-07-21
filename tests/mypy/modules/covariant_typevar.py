from typing import Generic, TypeVar

from whoop_pydantic_v2 import BaseModel

T = TypeVar("T", covariant=True)


class Foo(BaseModel, Generic[T]):
    value: T


class Bar(Foo[T]): ...
