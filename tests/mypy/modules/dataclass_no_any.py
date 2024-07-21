from whoop_pydantic_v2.dataclasses import dataclass


@dataclass
class Foo:
    foo: int


@dataclass(config={'title': 'Bar Title'})
class Bar:
    bar: str
