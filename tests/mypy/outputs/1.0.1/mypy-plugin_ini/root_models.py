from typing import List

from whoop_pydantic_v2 import RootModel


class Pets1(RootModel[List[str]]):
    pass


pets_construct = Pets1.model_construct(['dog'])

Pets2 = RootModel[List[str]]


class Pets3(RootModel):
# MYPY: error: Missing type parameters for generic type "RootModel"  [type-arg]
    root: List[str]


pets1 = Pets1(['dog', 'cat'])
pets2 = Pets2(['dog', 'cat'])
pets3 = Pets3(['dog', 'cat'])


class Pets4(RootModel[List[str]]):
    pets: List[str]
# MYPY: error: Only `root` is allowed as a field of a `RootModel`  [whoop_pydantic_v2-field]
