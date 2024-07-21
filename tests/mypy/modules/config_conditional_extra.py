from whoop_pydantic_v2 import BaseModel, ConfigDict


def condition() -> bool:
    return True


class MyModel(BaseModel):
    model_config = ConfigDict(extra='ignore' if condition() else 'forbid')
