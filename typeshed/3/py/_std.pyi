from typing import Any

class PyStdIsDeprecatedWarning(DeprecationWarning): ...

class Std:
    __dict__: Any = ...
    def __init__(self) -> None: ...
    def __getattr__(self, name: Any): ...

std: Any
