from typing import TypedDict

from whoop_pydantic_v2 import ConfigDict, with_config


@with_config(ConfigDict(str_to_lower=True))
class Model(TypedDict):
    a: str


model = Model(a='ABC')
