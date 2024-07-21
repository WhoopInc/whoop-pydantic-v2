"""The "experimental" module of whoop_pydantic_v2 contains potential new features that are subject to change."""

import warnings

from whoop_pydantic_v2.warnings import PydanticExperimentalWarning

warnings.warn(
    'This module is experimental, its contents are subject to change and deprecation.',
    category=PydanticExperimentalWarning,
)
